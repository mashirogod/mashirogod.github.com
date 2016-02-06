void __cdecl sub_8048C59(int type)
{
  struct_ptr *Pokemon1; // ST2C_4@2
  struct_buf *Pokemon2; // ST28_4@4

  if ( type == 1 )
  {
    Pokemon1 = (struct_ptr *)malloc(0x888u);
    Pokemon1->name = 'rahC';
    Pokemon1->name_ = 'razi';
    Pokemon1->name__ = 'd';
    strcpy(&Pokemon1->art, src);
    Pokemon1->dword880 = &off_804BF78;
    Pokemon1->HP? = 100;
    Pokemon1->dword87C = 10;
    Pokemon1->profile = Profile;
    Battle(Pokemon1, 1, Pokemon1->HP?, Pokemon1->dword87C, *(_DWORD *)Pokemon1->dword880, Pokemon1);
  }
  else if ( type == 2 )
  {
    Pokemon2 = (struct_buf *)malloc(0x214u);
    Pokemon2->dword0 = 'ukaK';
    Pokemon2->word4 = 'an';
    Pokemon2->byte6 = 0;
    strcpy(&Pokemon2->charF, a_________);
    Pokemon2->dword20C = &off_804BF7C;
    Pokemon2->dword204 = 20;
    Pokemon2->dword208 = 1;
    Pokemon2->dword210 = Profile_;
    Battle(Pokemon2, 2, Pokemon2->dword204, Pokemon2->dword208, *(_DWORD *)Pokemon2->dword20C, Pokemon2);
  }
}
