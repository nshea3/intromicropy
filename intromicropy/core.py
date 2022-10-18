# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_core.ipynb.

# %% auto 0
__all__ = ['supply', 'demand', 'find_equilibrium']

# %% ../nbs/00_core.ipynb 4
def supply(expr: str):
    sf_ = parse_expr(expr)
    assert "Q_s" in expr
    assert diff(sf_) > 0
    return sf_


def demand(expr: str):
    df_= parse_expr(expr)
    assert "Q_d" in expr
    assert diff(df_) < 0
    return df_


def find_equilibrium(sf, df):
    Qstar = sympy.Symbol("Q^*")
    df_star_ = df.subs({"Q_d":Qstar})
    sf_star_ = sf.subs({"Q_s":Qstar})
    eq = sympy.Eq(sf_star_, df_star_)
    return (sympy.solve(eq)[0], 
            df_star_.subs({Qstar : sympy.solve(eq)[0]}))


