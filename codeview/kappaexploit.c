int vuln_execute()
{
  int result; // eax@1
  signed int i; // [sp+1Ch] [bp-Ch]@1

  result = puts("Here are all of the stats on your current Pokemon!");
  for ( i = 0; i <= 4; ++i )
  {
    result = (int)*(&My_poke + i);
    if ( !result )
      break;
    if ( type_data[i] == 3 )
    {
      result = (*((int (__cdecl **)(_DWORD))*(&My_poke + i) + 0x17E))(*(&My_poke + i));
    }
    else if ( type_data[i] == 1 )
    {
      result = (*((int (__cdecl **)(_DWORD))*(&My_poke + i) + 0x221))(*(&My_poke + i));
    }
    else
    {
      result = type_data[i];
      if ( result == 2 )
        result = (*((int (__cdecl **)(_DWORD))*(&My_poke + i) + 132))(*(&My_poke + i));
    }
  }
  return result;
}
