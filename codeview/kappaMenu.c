void __cdecl main()
{
  setvbuf(stdout, 0, 2, 0);
  setvbuf(stdin, 0, 2, 0);
  sleep(1u);
  sub_80491F6();
  sub_80486DC();
  while ( 1 )
  {
    switch ( sub_804886E() )
    {
      case 0:
        sub_8048DE3();
        break;
      case 1:
        sub_8048F56();
        break;
      case 2:
        vuln_execute();
        break;
      case 3:
        advice();
        break;
      case 4:
        vulne_exploit();
        break;
      default:
        continue;
    }
  }
}
