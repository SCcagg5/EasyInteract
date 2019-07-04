from Model.basic import check
from Object.blockchain import block
from Object.cred import token

def verify(cn, nextc):
    err = check.contain(cn.pr, ["token"])
    if not err[0]:
        return cn.toret.add_error(err[1], err[2])
    cn.pr = err[1]

    use = token(cn.pr["token"])
    err = use.verify()
    return cn.call_next(nextc, err)

def login(cn, nextc):
    err = check.contain(cn.pr, [])
    if not err[0]:
        return cn.toret.add_error(err[1], err[2])
    cn.pr = err[1]

    use = token("")
    err = use.login()
    return cn.call_next(nextc, err)

def addmodel(cn, nextc):
    err = check.contain(cn.pr, ["address", "model"])
    if not err[0]:
        return cn.toret.add_error(err[1], err[2])
    cn.pr = err[1]

    use = block(cn.pr["address"])
    err = use.upload(cn.pr["model"])
    return cn.call_next(nextc, err)

def askmoney(cn, nextc):
    err = check.contain(cn.pr, ["address"])
    if not err[0]:
        return cn.toret.add_error(err[1], err[2])
    cn.pr = err[1]

    use = block(cn.pr["address"])
    err = use.get_data("balanceNQT")
    return cn.call_next(nextc, err)
