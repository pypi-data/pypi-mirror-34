"""The main module to build a simplelife model.

This module contains only one function :py:func:`build`,
which creates a model from source modules and return it.

If this module is run as a script, the :py:func:`build` function is called
and the created model is available as ``model`` global variable.
"""
import os
import modelx as mx

def build(load_saved=False):
    """Build a model and return it.

    Read input data from `input.xlsm`, create `Input` space and its
    subspace and cells and populate them with the data.

    Args:
        load_saved: If ``True``, input data is read from `ifrs17sim.mx` file
            instead of `input.xlsm`, which is saved when
            :py:func:`build_input <simplelife.build_input.build_input>`
            is executed last time. Defaults to ``False``
    """

    # Make sure the current directory is this folder
    os.chdir(os.path.abspath(os.path.dirname(__file__)))

    # ------------------------------------------------------------------------
    # Build Input space

    from build_input import build_input

    if load_saved:
        model = mx.open_model('ifrs17sim.mx')
        input = model.Input
    else:
        model = mx.new_model(name='ifrs17sim')
        input = build_input(model, 'input.xlsm')
        model.save('ifrs17sim.mx')

    # ------------------------------------------------------------------------
    # Build CommFunc space

    lifetable_refs = {'Input': input}

    def lifetable_params(Sex, IntRate, TableID):
        refs={'MortalityTable': Input.MortalityTables(TableID).MortalityTable}
        return {'refs': refs}

    lifetable = model.import_module(
        module_='lifetable',
        name='LifeTable',
        formula=lifetable_params,
        refs=lifetable_refs)

    # ------------------------------------------------------------------------
    # Build Policy space

    from policy import policy_attrs

    policy_refs = {'PolicyData': input.PolicyData,
                   'ProductSpec': input.ProductSpec,
                   'LifeTable': lifetable,
                   'PolicyAttrs': policy_attrs}

    def policy_params(PolicyID):
        refs = {attr: PolicyData[PolicyID].cells[attr] for attr in PolicyAttrs}
        alias = {'PremTerm': refs['PolicyTerm'],
                 'x': refs['IssueAge'],
                 'm': refs['PolicyTerm'],
                 'n': refs['PolicyTerm']}

        refs.update(alias)
        return {'refs': refs}

    policy = model.import_module(
        module_='policy',
        name='Policy',
        formula=policy_params,
        refs=policy_refs)

    # ------------------------------------------------------------------------
    # Build Assumption space

    asmp_refs = {'Policy': policy,
                 'ProductSpec': input.ProductSpec,
                 'MortalityTables': input.MortalityTables,
                 'asmp': input.Assumption,
                 'asmp_tbl': input.AssumptionTables}

    def asmp_params(PolicyID):
        refs = {'pol': Policy[PolicyID]}
        alias = {'prod': refs['pol'].Product,
                 'polt': refs['pol'].PolicyType,
                 'gen': refs['pol'].Gen}
        refs.update(alias)
        return {'refs': refs}

    asmp = model.import_module(
        module_='assumption',
        name='Assumption',
        formula=asmp_params,
        refs=asmp_refs)

    asmp.allow_none = True

    # ------------------------------------------------------------------------
    # Build Assumption space

    def econ_params(ScenID):
        refs = {'Scenario': Input.Scenarios[ScenID]}
        return {'refs': refs}

    economic = model.import_module(
        module_='economic',
        name='Economic',
        formula=econ_params,
        refs={'asmp': asmp,
              'Input': input})

    # ------------------------------------------------------------------------
    # Build Projection space
    
    # Model tree structure
    # 
    # lifelib --+
    #           +--BaseProj
    #           +--OuterProj[PolicyID] <--- BaseProj
    #                    +--InnerProj[t] <-- BaseProj

    proj_refs = {'Pol': policy,
                 'Asmp': asmp,
                 'Scen': economic}

    def proj_params(PolicyID, ScenID=1):
        refs = {'pol': Pol[PolicyID],
                'asmp': Asmp[PolicyID],
                'scen': Scen[ScenID]}

        return {'refs': refs}

    baseproj = model.import_module(
        module_='projection',
        name='BaseProj')

    ifrs = model.import_module(
        module_='ifrs',
        name='IFRS')

    outerproj = model.new_space(
        bases=[ifrs, baseproj],
        name='OuterProj',
        formula=proj_params,
        refs=proj_refs)

    def innerproj_params(t0):
        refs = {'pol': _self.parent.pol,
                'asmp': _self.parent.asmp,
                'scen': _self.parent.scen,
                'outer': _self.parent}
        
        return {'refs': refs}

    innerproj = outerproj.new_space(
        bases=baseproj,
        name='InnerProj',
        formula=innerproj_params)

    pvs = innerproj.import_module(
        module_='present_value',
        name='PresentValue')
    
    def pvs_params(t_rate):
        refs = {'last_t': _self.parent.last_t,
                'InsurIF_Beg1': _self.parent.InsurIF_Beg1,
                'InsurIF_End': _self.parent.InsurIF_End,
                'PremIncome': _self.parent.PremIncome,
                'BenefitSurr': _self.parent.BenefitSurr,
                'BenefitDeath': _self.parent.BenefitDeath,
                'BenefitTotal': _self.parent.BenefitTotal,
                'ExpsCommTotal': _self.parent.ExpsCommTotal,
                'ExpsAcq': _self.parent.ExpsAcq,
                'ExpsMaint': _self.parent.ExpsMaint,
                'ExpsTotal': _self.parent.ExpsTotal,
                'DiscRate': _self.parent.scen.DiscRate}
        
        return {'refs': refs}
        
    pvs.set_formula(pvs_params)
    
    return model


if __name__ == '__main__':
    model = build()
