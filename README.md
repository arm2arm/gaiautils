# gaiautils
gaia.aip.de cheatsheet

# Convert gaia source_id to healpix ID
* more info please check esac docs: https://gea.esac.esa.int/archive/documentation/GEDR3/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html
```
hpix  = source_id / (235×4(12−n)) = source_id / 2**(59−2n)
```

# Usage 
in order to make a loop over the all sky you should go over the hpix one by one:
in this seudocode example you will get with HpixLevel=5  12288 spllits, replresenting an individual healpix tiles.
```
HpixLevel=5
NPIX = 12*4**HpixLevel

for i in range(0,NPIX):
   data=make_one_query()
   save_data(f"level_{HpixLevel}_hpix_{i}.h5")
```
