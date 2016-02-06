 puts("What would you like to name this Pokemon?");
  *((_BYTE *)argv2 + read(0, argv2, 0xEu)) = 0;
  for ( i = 0; i <= 4; ++i )
  {
    if ( !*(&My_poke + i) )
    {
      *(&My_poke + i) = argv1;
      type_data[i] = a2;
      return;
    }
  }
  puts("Oh no! you don't have any more room for a Pokemon! Choose a pokemon to replace!");
  v7 = sub_80488C9();
  if ( v7 )
  {
    if ( v7 <= 4 )
    {
      free(*(&My_poke + v7));
      *(&My_poke + v7) = argv1;
    }
    else
    {
      puts("Invalid Choice!");
    }
  }
