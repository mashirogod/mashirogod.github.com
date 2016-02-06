int change_art()
{
  ssize_t v0; // eax@2
  char src[4000]; // [sp+10h] [bp-FB8h]@2
  size_t n; // [sp+FB0h] [bp-18h]@1
  int v4; // [sp+FB4h] [bp-14h]@1
  int v5; // [sp+FB8h] [bp-10h]@1
  size_t i; // [sp+FBCh] [bp-Ch]@1

  v5 = sub_80488C9();
  v4 = (int)*(&My_poke + v5);
  n = strlen((const char *)(v4 + 15));
  for ( i = 0; i < n; i += v0 )
    v0 = read(0, &src[i], n - i);
  memcpy((void *)(v4 + 15), src, n);
  *(_BYTE *)(v4 + n + 15) = 0;
  return puts("I'm sure you'll love to show this new art to your friends!");
}
