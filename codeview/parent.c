  if ( read(0, &buf, 4uLL) > 0 )
  {
    v3 = (char *)buf;
    v11 = (char *)mmap(0LL, buf, 7, 34, -1, 0LL);
    if ( !v11 )
      __assert_fail("psc != ((void *)0)", "sandman.c", 0xCAu, "main");
    v13 = 0;
    while ( buf )
    {
      v3 = &v11[v13];
      v12 = read(0, v3, buf);
      if ( v12 < 0 )
        break;
      v13 += v12;
      buf -= v12;
    }
    if ( !buf )
    {
      LODWORD(v4) = seccomp_init(0LL, v3);
      v10 = v4;
      if ( v4 )
      {
        v12 = seccomp_rule_add(v10, 2147418112LL, 0LL, 0LL);
        if ( v12 >= 0 )
        {
          v12 = seccomp_rule_add(v10, 2147418112LL, 1LL, 0LL);
          if ( v12 >= 0 )
          {
            v12 = seccomp_rule_add(v10, 2147418112LL, 60LL, 0LL);
            if ( v12 >= 0 )
            {
              v12 = seccomp_rule_add(v10, 2147418112LL, 231LL, 0LL);
              if ( v12 >= 0 )
              {
                v5 = v10;
                v12 = seccomp_load(v10);
                if ( v12 >= 0 )
                {
                  v9 = v11;
                  ((void (__fastcall *)(__int64, signed __int64))v11)(v5, 2147418112LL);
                }
              }
            }
          }
        }
      }
    }
  }
