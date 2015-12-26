void sub_8048DE3()
{
  puts("You walk into the tall grass!");
  sleep(1u);
  puts(".");
  sleep(1u);
  puts(".");
  sleep(1u);
  puts(".");
  sleep(1u);
  if ( ++dword_804BFA8 % 13 )
  {
    if ( dword_804BFA8 & 1 )
      puts("You failed to find any Pokemon!");
    else
      sub_8048C59(2);
  }
  else
  {
    sub_8048C59(1);
  }
}
