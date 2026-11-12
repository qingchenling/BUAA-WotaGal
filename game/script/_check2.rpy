init 999 python:
    import io as _io
    with _io.open("C:/Users/admin/Documents/deepseek-harness/default-workspace/check2.txt", "w", encoding="utf-8") as _f:
        for _n in ("MAP_ZOOM", "MAP_LOCATIONS", "LOC_YONGMAN", "LOC_SKY", "LOC_BEIJING"):
            _f.write("%s = %s\n" % (_n, "存在" if _n in globals() else "缺失"))
        try:
            _f.write("len(MAP_LOCATIONS)=%d\n" % len(MAP_LOCATIONS))
        except Exception as _e:
            _f.write("len err %r\n" % _e)
