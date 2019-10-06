from pwn import *
import gmpy2

c = 43441542775783232206540746077054219922289399027741516367215694612444663222391576437869116419214149901308503288544047378091571103398210769014712729972178653544269352540701439571110764931761674102874563099362843887401539105985685271250166764111125778239217963933343030203036637058692099141635014724767619946722695502929848993358384590852732486209
e = 65537
n = 54456940799326662059914964803646773423443978848582114925951419870771458650311967705813353346224861972786044431727523001635213412519381806070932130509129505061271430458880278532308839822916165403085759824822373603393782931610671244949013315204941117015878770557923629379383104292602716471323140319822960810055879795308417671316110851825901350249
#https://www.alpertron.com.ar/ECM.HTM
r = [8614232867,9559889953,9664899577,10240616653,10575596639,10625592067,10675053677,10908009247,10932876959,11309131781,11424408761,11951753909,12059355361,12065470493,12074461613,12237291839,12932137973,13097274991,13486974533,13792570217,14091419621,14609238781,14726553067,14981814767,15027138937,15212529191,15453873223,15590768729,15654356749,15793577729,15878402983,16064628949,16640346761,17007443317]

assert(n == reduce(lambda x, y: x * y, r))

phi_n = 1
for i in range(len(r)):
    phi_n *= (r[i] - 1)
log.info("phi_n: {}".format(phi_n))

d = gmpy2.invert(e, phi_n)
log.info("d: {}".format(d))

plaintext = pow(c, d, n)
log.info("plaintext: {}".format(str(plaintext)))
plaintext_decoded = (format(plaintext, 'x')).decode("hex")
log.success("Flag: {}".format(plaintext_decoded))