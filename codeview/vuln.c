  for ( i = 0; i <= 0x13; ++i )
  {
    printf("[FREE][address=%X]\n", *(&v4 + 2 * i));
    free((void *)*(&v4 + 2 * i));
  }
