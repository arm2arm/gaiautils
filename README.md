# gaiautils
gaia.aip.de cheatsheet

# Convert gaia source_id to healpix ID
* more info please check esac docs: https://gea.esac.esa.int/archive/documentation/GEDR3/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html
```
hpix  = source_id / (235×4(12−n)) = source_id / 2**(59−2n)
```
