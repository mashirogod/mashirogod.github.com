int __fastcall sub_400BAC(__int64 a1)
{
  int result; // eax@1
  char *v2; // rax@4
  char *v3; // rax@6
  size_t v4; // rax@9
  char dest; // [sp+10h] [bp-220h]@9
  size_t v6; // [sp+210h] [bp-20h]@2
  char *nptr; // [sp+218h] [bp-18h]@2
  char *v8; // [sp+220h] [bp-10h]@1
  unsigned __int16 v9; // [sp+22Eh] [bp-2h]@1

  v9 = 80;
  v8 = (char *)&unk_401194;
  result = strncmp((const char *)a1, "http://", 7uLL);
  if ( !result )
  {
    nptr = (char *)(a1 + 7);
    v6 = a1 + strlen((const char *)a1);
    while ( (unsigned __int64)nptr > v6 )
    {
      if ( *nptr == 0x3A )
      {
        v2 = nptr++;
        *v2 = 0;
        v9 = atoi(nptr);
      }
      else if ( *nptr == 0x2F )
      {
        v3 = nptr++;
        *v3 = 0;
        v8 = nptr;
        break;
      }
      ++nptr;
    }
    nptr = (char *)(a1 + 7);
    v4 = strlen((const char *)(a1 + 7));
    strncpy(&dest, (const char *)(a1 + 7), v4);
    result = sub_400B97((__int64)&dest, v9);
  }
  return result;
}
