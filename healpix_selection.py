
#Select all stars within the hpnum healpix level 5 tile
hpnum=1
level=5
sid_inf=hpnum*2**35*4**(12-level)
sid_sup=(hpnum+1)*2**35*4**(12-level)

query="SELECT gaia.source_id FROM gaiaedr3.gaia_source as gaia AND gaia.phot_g_mean_mag < 18"+\
      " AND gaia.source_id BETWEEN {} AND {}".format(sid_inf,sid_sup)
