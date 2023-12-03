like in level 1, we have a program that input the user for a password and answers "Nope." or "Good job." depending on whether the right answer is found or not

however, this time the program is a bit more complex.
When we look at the program strings, there are huge latin paragraphs in addition to the Nope, Good job, please enter the key strings.
There is also a single word : "delabere"

and when looking at the program functions, we see a lot of custom functions (xd, xxd, xxxd, ...)
```bash
level2 git:(main) ✗ nm level2 
000001cc r __abi_tag
         U atoi@GLIBC_2.0
0000703c B __bss_start
0000703c b completed.0
         w __cxa_finalize@GLIBC_2.1.3
00007034 D __data_start
00007034 W data_start
00001130 t deregister_tm_clones
000011c0 t __do_global_dtors_aux
00006ef4 d __do_global_dtors_aux_fini_array_entry
00007038 D __dso_handle
00006ef8 d _DYNAMIC
0000703c D _edata
00007040 B _end
         U exit@GLIBC_2.0
         U fflush@GLIBC_2.0
000015ec T _fini
00002000 R _fp_hw
00001210 t frame_dummy
00006ef0 d __frame_dummy_init_array_entry
00005688 r __FRAME_END__
00007000 d _GLOBAL_OFFSET_TABLE_
         w __gmon_start__
00005494 r __GNU_EH_FRAME_HDR
00001000 T _init
00002004 R _IO_stdin_used
         U __isoc99_scanf@GLIBC_2.7
         w _ITM_deregisterTMCloneTable
         w _ITM_registerTMCloneTable
         U __libc_start_main@GLIBC_2.34
000012d0 T main
         U memset@GLIBC_2.0
000014d0 T n
00001220 T no
000012a0 T ok
         U printf@GLIBC_2.0
         U puts@GLIBC_2.0
00001170 t register_tm_clones
000010f0 T _start
         U stdin@GLIBC_2.0
         U strcmp@GLIBC_2.0
         U strlen@GLIBC_2.0
0000703c D __TMC_END__
00001540 T ww
00001120 T __x86.get_pc_thunk.bx
00001219 T __x86.get_pc_thunk.dx
00001260 T xd
00001490 T xxd
00001500 T xxxd
000015b0 T xyxxd
```

However, when looking at the main, we see that the only custom functions that are called are ok() and no(), we will therefore ignore the other functions.
When looking at the functions with objdump :
```bash
objdump level2 --disassemble=no 

level2:     file format elf32-i386


Disassembly of section .init:

Disassembly of section .plt:

Disassembly of section .plt.got:

Disassembly of section .text:

00001220 <no>:
    1220:       55                      push   %ebp
    1221:       89 e5                   mov    %esp,%ebp
    1223:       53                      push   %ebx
    1224:       83 ec 14                sub    $0x14,%esp
    1227:       e8 00 00 00 00          call   122c <no+0xc>
    122c:       5b                      pop    %ebx
    122d:       81 c3 d4 5d 00 00       add    $0x5dd4,%ebx
    1233:       89 5d f8                mov    %ebx,-0x8(%ebp)
    1236:       8d 83 08 b0 ff ff       lea    -0x4ff8(%ebx),%eax
    123c:       89 04 24                mov    %eax,(%esp)
    123f:       e8 3c fe ff ff          call   1080 <puts@plt>
    1244:       8b 5d f8                mov    -0x8(%ebp),%ebx
    1247:       c7 04 24 01 00 00 00    movl   $0x1,(%esp)
    124e:       e8 3d fe ff ff          call   1090 <exit@plt>

Disassembly of section .fini:
```

```bash
 level2 git:(main) ✗ objdump level2 --disassemble=ok

level2:     file format elf32-i386


Disassembly of section .init:

Disassembly of section .plt:

Disassembly of section .plt.got:

Disassembly of section .text:

000012a0 <ok>:
    12a0:       55                      push   %ebp
    12a1:       89 e5                   mov    %esp,%ebp
    12a3:       53                      push   %ebx
    12a4:       50                      push   %eax
    12a5:       e8 00 00 00 00          call   12aa <ok+0xa>
    12aa:       5b                      pop    %ebx
    12ab:       81 c3 56 5d 00 00       add    $0x5d56,%ebx
    12b1:       8d 83 11 bd ff ff       lea    -0x42ef(%ebx),%eax
    12b7:       89 04 24                mov    %eax,(%esp)
    12ba:       e8 c1 fd ff ff          call   1080 <puts@plt>
    12bf:       83 c4 04                add    $0x4,%esp
    12c2:       5b                      pop    %ebx
    12c3:       5d                      pop    %ebp
    12c4:       c3                      ret    

Disassembly of section .fini:
```

both ok() and no() displays text to the screen using puts. The only difference is that no() exit the program at the end, while the ok function returns.
It is safe to assume that no() prints "Nope." and ok() prints "Good job."


```bash
   0x565562d0 <+0>:     push   %ebp
   0x565562d1 <+1>:     mov    %esp,%ebp
   0x565562d3 <+3>:     push   %ebx
=> 0x565562d4 <+4>:     sub    $0x54,%esp
   0x565562d7 <+7>:     call   0x565562dc <main+12>
   0x565562dc <+12>:    pop    %ebx
   0x565562dd <+13>:    add    $0x5d24,%ebx
   0x565562e3 <+19>:    mov    %ebx,-0x40(%ebp)
   0x565562e6 <+22>:    movl   $0x0,-0x8(%ebp)
   0x565562ed <+29>:    lea    -0x42e5(%ebx),%eax
   0x565562f3 <+35>:    mov    %eax,(%esp)
   0x565562f6 <+38>:    call   0x56556060 <printf@plt> #print the prompt for a key
   0x565562fb <+43>:    mov    -0x40(%ebp),%ebx
   0x565562fe <+46>:    lea    -0x35(%ebp),%eax
   0x56556301 <+49>:    lea    -0x42d2(%ebx),%ecx
   0x56556307 <+55>:    mov    %ecx,(%esp)
   0x5655630a <+58>:    mov    %eax,0x4(%esp)
   0x5655630e <+62>:    call   0x565560c0 <__isoc99_scanf@plt> # takes user input
   0x56556313 <+67>:    mov    %eax,-0xc(%ebp)
   0x56556316 <+70>:    mov    $0x1,%eax 
   0x5655631b <+75>:    cmp    -0xc(%ebp),%eax # compare return of scanf with 1 (0x1), if it is the case, jump to main+92, else move along in the program
   0x5655631e <+78>:    je     0x5655632c <main+92>
   0x56556324 <+84>:    mov    -0x40(%ebp),%ebx
   0x56556327 <+87>:    call   0x56556220 <no> # call no function if the return of scanf was different than 1
   0x5655632c <+92>:    movsbl -0x34(%ebp),%ecx # move the 4 bits unit at adress ebp -0x34 to ecx, if we inspect x/s $ebp - 0x34, it is "onjour" which the string I passed without the 1st char
   0x56556330 <+96>:    mov    $0x30,%eax # store 0x30 in eax
   0x56556335 <+101>:   cmp    %ecx,%eax # compare eax to ecx, ecx contains the hexadecimal equivalent of the first character of "onjour" which is 0x6f ('o' in hexa)
   0x56556337 <+103>:   je     0x56556345 <main+117>
   0x5655633d <+109>:   mov    -0x40(%ebp),%ebx
   0x56556340 <+112>:   call   0x56556220 <no> # if not equal, prints no --> 2nd character of the passed string must be 0x30, that is '0'
   0x56556345 <+117>:   movsbl -0x35(%ebp),%ecx # repeats the process with the previous character -> first character must also be '0'
   0x56556349 <+121>:   mov    $0x30,%eax
   0x5655634e <+126>:   cmp    %ecx,%eax
   0x56556350 <+128>:   je     0x5655635e <main+142>
   0x56556356 <+134>:   mov    -0x40(%ebp),%ebx
   0x56556359 <+137>:   call   0x56556220 <no>
   0x5655635e <+142>:   mov    -0x40(%ebp),%ebx
   0x56556361 <+145>:   mov    -0xc(%ebx),%eax
   0x56556367 <+151>:   mov    (%eax),%eax
   0x56556369 <+153>:   mov    -0xc(%ebx),%ecx
   0x5655636f <+159>:   mov    %eax,(%esp)
   0x56556372 <+162>:   call   0x56556070 <fflush@plt>
   0x56556377 <+167>:   mov    -0x40(%ebp),%ebx
   0x5655637a <+170>:   lea    -0x1d(%ebp),%eax
   0x5655637d <+173>:   xor    %ecx,%ecx
   0x5655637f <+175>:   mov    %eax,(%esp)
   0x56556382 <+178>:   movl   $0x0,0x4(%esp)
   0x5655638a <+186>:   movl   $0x9,0x8(%esp)
   0x56556392 <+194>:   call   0x565560b0 <memset@plt> # for the remaining of the program, I used ghidra as well to make understanding the program easier. This line sets each char of a 9 char array to the value 0 ('\0')
   0x56556397 <+199>:   movb   $0x64,-0x1d(%ebp) # set the first char of the array used in memset to 'd'
   0x5655639b <+203>:   movb   $0x0,-0x36(%ebp) 
   0x5655639f <+207>:   movl   $0x2,-0x14(%ebp) # initialize a variable to 2, it will be used to iterate over our passed string (starting from the 2nd character, as first 2 must be '0')
   0x565563a6 <+214>:   movl   $0x1,-0x10(%ebp) # initialize a variable to 1, it will be used to iterate over the array that was memset to store 9 characters (the first one is already defined and is a 'd')
   0x565563ad <+221>:   mov    -0x40(%ebp),%ebx
   0x565563b0 <+224>:   lea    -0x1d(%ebp),%ecx
   0x565563b3 <+227>:   mov    %esp,%eax
   0x565563b5 <+229>:   mov    %ecx,(%eax)
   0x565563b7 <+231>:   call   0x565560a0 <strlen@plt> # call strlen on the string stored in the array that was initialized in memset, for now the string is "d" -> returns 1
   0x565563bc <+236>:   mov    %eax,%ecx
   0x565563be <+238>:   xor    %eax,%eax
   0x565563c0 <+240>:   cmp    $0x8,%ecx # compare the value of strlen with 8
   0x565563c3 <+243>:   mov    %al,-0x41(%ebp)
   0x565563c6 <+246>:   jae    0x565563ee <main+286> # if value above or equal, that means if strlen >= 8, go to main + 286
   0x565563cc <+252>:   mov    -0x40(%ebp),%ebx
   0x565563cf <+255>:   mov    -0x14(%ebp),%eax
   0x565563d2 <+258>:   mov    %eax,-0x48(%ebp)
   0x565563d5 <+261>:   lea    -0x35(%ebp),%ecx
   0x565563d8 <+264>:   mov    %esp,%eax
   0x565563da <+266>:   mov    %ecx,(%eax)
   0x565563dc <+268>:   call   0x565560a0 <strlen@plt> # if strlen < 8, call strlen again but this time if we inspect $ecx (x/s $ecx, it is with out input passed)
   0x565563e1 <+273>:   mov    %eax,%ecx
   0x565563e3 <+275>:   mov    -0x48(%ebp),%eax
   0x565563e6 <+278>:   cmp    %ecx,%eax # compare the result of strlen (in ecx, with the value in eax, which is -0x48(%ebp), which if we look at +255 and +258 is -0x14(%ebp), which is our counter that was initialized to 2. In fact, we just check if we have traversed our whole imput or not)
   0x565563e8 <+280>:   setb   %al
   0x565563eb <+283>:   mov    %al,-0x41(%ebp)
   0x565563ee <+286>:   mov    -0x41(%ebp),%al
   0x565563f1 <+289>:   test   $0x1,%al
   0x565563f3 <+291>:   jne    0x565563fe <main+302>
   0x565563f9 <+297>:   jmp    0x5655644a <main+378> # if the value is higher than the len, we have seen all the input and we move to the end, else we continue
   0x565563fe <+302>:   mov    -0x40(%ebp),%ebx
   0x56556401 <+305>:   mov    -0x14(%ebp),%eax
   0x56556404 <+308>:   mov    -0x35(%ebp,%eax,1),%al
   0x56556408 <+312>:   mov    %al,-0x39(%ebp)
   0x5655640b <+315>:   mov    -0x14(%ebp),%eax
   0x5655640e <+318>:   mov    -0x34(%ebp,%eax,1),%al
   0x56556412 <+322>:   mov    %al,-0x38(%ebp)
   0x56556415 <+325>:   mov    -0x14(%ebp),%eax
   0x56556418 <+328>:   mov    -0x33(%ebp,%eax,1),%al
   0x5655641c <+332>:   mov    %al,-0x37(%ebp)
   0x5655641f <+335>:   lea    -0x39(%ebp),%eax
   0x56556422 <+338>:   mov    %eax,(%esp)
   0x56556425 <+341>:   call   0x565560d0 <atoi@plt> # when inspecting $eax, the value pass to atoi is the string formed by the first 3 characters of our input after the 2 '0', we will then store the value in the array that was memset before. We then repeat the process but we increment the counter that traverses our input by 3, to read chars by group of 3 (decimal code of each character), and the counter that traverses the memset array by one
   0x5655642a <+346>:   mov    %al,%cl
   0x5655642c <+348>:   mov    -0x10(%ebp),%eax
   0x5655642f <+351>:   mov    %cl,-0x1d(%ebp,%eax,1)
   0x56556433 <+355>:   mov    -0x14(%ebp),%eax
   0x56556436 <+358>:   add    $0x3,%eax
   0x56556439 <+361>:   mov    %eax,-0x14(%ebp)
   0x5655643c <+364>:   mov    -0x10(%ebp),%eax
   0x5655643f <+367>:   add    $0x1,%eax
   0x56556442 <+370>:   mov    %eax,-0x10(%ebp)
   0x56556445 <+373>:   jmp    0x565563ad <main+221>
   0x5655644a <+378>:   mov    -0x40(%ebp),%ebx
   0x5655644d <+381>:   mov    -0x10(%ebp),%eax
   0x56556450 <+384>:   movb   $0x0,-0x1d(%ebp,%eax,1)
   0x56556455 <+389>:   lea    -0x1d(%ebp),%ecx
   0x56556458 <+392>:   lea    -0x42cd(%ebx),%edx
   0x5655645e <+398>:   mov    %esp,%eax
   0x56556460 <+400>:   mov    %edx,0x4(%eax)
   0x56556463 <+403>:   mov    %ecx,(%eax)
   0x56556465 <+405>:   call   0x56556040 <strcmp@plt> # it compares the resulting memset array to "delabere" and calls the function ok if it matches and the fonction no otherwise
   0x5655646a <+410>:   cmp    $0x0,%eax
   0x5655646d <+413>:   jne    0x56556480 <main+432>
   0x56556473 <+419>:   mov    -0x40(%ebp),%ebx
   0x56556476 <+422>:   call   0x565562a0 <ok>
   0x5655647b <+427>:   jmp    0x56556488 <main+440>
   0x56556480 <+432>:   mov    -0x40(%ebp),%ebx
   0x56556483 <+435>:   call   0x56556220 <no>
   0x56556488 <+440>:   xor    %eax,%eax
   0x5655648a <+442>:   add    $0x54,%esp
   0x5655648d <+445>:   pop    %ebx
   0x5655648e <+446>:   pop    %ebp
   0x5655648f <+447>:   ret
```

the goal of the program is therefore to write "elabere" in ascii (the first 'd' is given by the program so to speak), with 2 leading '0' to pass the first test and in one word so that scanf returns 1
therefore we can pass : 00101108097098101114101
-> 101: e
-> 108: l
-> 097: a (we need to write it with 3 digits each time)
-> 098: b
-> 101: e
-> 114: r
-> 101: e