the functioning of the binary is the same as the first 2 programs
and once again, when looking at the functions, we see multiple custom functions

```bash
➜  level3 git:(main) ✗ nm level3 
000000000000037c r __abi_tag
                 U atoi@GLIBC_2.2.5
0000000000004070 B __bss_start
0000000000001220 T but
0000000000004070 b completed.0
                 w __cxa_finalize@GLIBC_2.2.5
0000000000004060 D __data_start
0000000000004060 W data_start
0000000000001100 t deregister_tm_clones
0000000000001170 t __do_global_dtors_aux
0000000000003de8 d __do_global_dtors_aux_fini_array_entry
0000000000004068 D __dso_handle
0000000000003df0 d _DYNAMIC
00000000000012c0 T easy
0000000000004070 D _edata
0000000000004078 B _end
                 U exit@GLIBC_2.2.5
                 U fflush@GLIBC_2.2.5
0000000000001580 T _fini
00000000000011b0 t frame_dummy
0000000000003de0 d __frame_dummy_init_array_entry
00000000000022cc r __FRAME_END__
0000000000004000 d _GLOBAL_OFFSET_TABLE_
                 w __gmon_start__
000000000000205c r __GNU_EH_FRAME_HDR
0000000000001000 T _init
0000000000002000 R _IO_stdin_used
                 U __isoc99_scanf@GLIBC_2.7
0000000000001260 T it
                 w _ITM_deregisterTMCloneTable
                 w _ITM_registerTMCloneTable
                 U __libc_start_main@GLIBC_2.34
0000000000001320 T main
                 U memset@GLIBC_2.2.5
00000000000011e0 T nice
0000000000001280 T not
                 U printf@GLIBC_2.2.5
                 U puts@GLIBC_2.2.5
0000000000001130 t register_tm_clones
00000000000010d0 T _start
                 U stdin@GLIBC_2.2.5
                 U strcmp@GLIBC_2.2.5
                 U strlen@GLIBC_2.2.5
0000000000001300 T ____syscall_malloc
00000000000012e0 T ___syscall_malloc
00000000000012a0 T that
0000000000001240 T this
0000000000004070 D __TMC_END__
0000000000001200 T try
00000000000011c0 T wt
```

```bash
objdump level3 --disassemble=main 

level3:     file format elf64-x86-64


Disassembly of section .init:

Disassembly of section .plt:

Disassembly of section .plt.got:

Disassembly of section .text:

0000000000001320 <main>:
    1320:       55                      push   %rbp
    1321:       48 89 e5                mov    %rsp,%rbp
    1324:       48 83 ec 60             sub    $0x60,%rsp
    1328:       c7 45 fc 00 00 00 00    movl   $0x0,-0x4(%rbp)
    132f:       48 8d 3d 0d 0d 00 00    lea    0xd0d(%rip),%rdi        # 2043 <_IO_stdin_used+0x43>
    1336:       b0 00                   mov    $0x0,%al
    1338:       e8 13 fd ff ff          call   1050 <printf@plt>
    133d:       48 8d 75 c0             lea    -0x40(%rbp),%rsi
    1341:       48 8d 3d 0e 0d 00 00    lea    0xd0e(%rip),%rdi        # 2056 <_IO_stdin_used+0x56>
    1348:       b0 00                   mov    $0x0,%al
    134a:       e8 51 fd ff ff          call   10a0 <__isoc99_scanf@plt>
    134f:       89 45 f8                mov    %eax,-0x8(%rbp)
    1352:       b8 01 00 00 00          mov    $0x1,%eax
    1357:       3b 45 f8                cmp    -0x8(%rbp),%eax
    135a:       0f 84 05 00 00 00       je     1365 <main+0x45>
    1360:       e8 7b ff ff ff          call   12e0 <___syscall_malloc>
    1365:       0f be 4d c1             movsbl -0x3f(%rbp),%ecx
    1369:       b8 32 00 00 00          mov    $0x32,%eax
    136e:       39 c8                   cmp    %ecx,%eax
    1370:       0f 84 05 00 00 00       je     137b <main+0x5b>
    1376:       e8 65 ff ff ff          call   12e0 <___syscall_malloc>
    137b:       0f be 4d c0             movsbl -0x40(%rbp),%ecx
    137f:       b8 34 00 00 00          mov    $0x34,%eax
    1384:       39 c8                   cmp    %ecx,%eax
    1386:       0f 84 05 00 00 00       je     1391 <main+0x71>
    138c:       e8 4f ff ff ff          call   12e0 <___syscall_malloc>
    1391:       48 8b 05 48 2c 00 00    mov    0x2c48(%rip),%rax        # 3fe0 <stdin@GLIBC_2.2.5>
    1398:       48 8b 38                mov    (%rax),%rdi
    139b:       e8 e0 fc ff ff          call   1080 <fflush@plt>
    13a0:       48 8d 7d df             lea    -0x21(%rbp),%rdi
    13a4:       31 f6                   xor    %esi,%esi
    13a6:       ba 09 00 00 00          mov    $0x9,%edx
    13ab:       e8 b0 fc ff ff          call   1060 <memset@plt>
    13b0:       c6 45 df 2a             movb   $0x2a,-0x21(%rbp)
    13b4:       c6 45 bf 00             movb   $0x0,-0x41(%rbp)
    13b8:       48 c7 45 e8 02 00 00    movq   $0x2,-0x18(%rbp)
    13bf:       00 
    13c0:       c7 45 f4 01 00 00 00    movl   $0x1,-0xc(%rbp)
    13c7:       48 8d 7d df             lea    -0x21(%rbp),%rdi
    13cb:       e8 70 fc ff ff          call   1040 <strlen@plt>
    13d0:       48 89 c1                mov    %rax,%rcx
    13d3:       31 c0                   xor    %eax,%eax
    13d5:       48 83 f9 08             cmp    $0x8,%rcx
    13d9:       88 45 bb                mov    %al,-0x45(%rbp)
    13dc:       0f 83 21 00 00 00       jae    1403 <main+0xe3>
    13e2:       48 8b 45 e8             mov    -0x18(%rbp),%rax
    13e6:       48 89 45 b0             mov    %rax,-0x50(%rbp)
    13ea:       48 8d 7d c0             lea    -0x40(%rbp),%rdi
    13ee:       e8 4d fc ff ff          call   1040 <strlen@plt>
    13f3:       48 89 c1                mov    %rax,%rcx
    13f6:       48 8b 45 b0             mov    -0x50(%rbp),%rax
    13fa:       48 39 c8                cmp    %rcx,%rax
    13fd:       0f 92 c0                setb   %al
    1400:       88 45 bb                mov    %al,-0x45(%rbp)
    1403:       8a 45 bb                mov    -0x45(%rbp),%al
    1406:       a8 01                   test   $0x1,%al
    1408:       0f 85 05 00 00 00       jne    1413 <main+0xf3>
    140e:       e9 4e 00 00 00          jmp    1461 <main+0x141>
    1413:       48 8b 45 e8             mov    -0x18(%rbp),%rax
    1417:       8a 44 05 c0             mov    -0x40(%rbp,%rax,1),%al
    141b:       88 45 bc                mov    %al,-0x44(%rbp)
    141e:       48 8b 45 e8             mov    -0x18(%rbp),%rax
    1422:       8a 44 05 c1             mov    -0x3f(%rbp,%rax,1),%al
    1426:       88 45 bd                mov    %al,-0x43(%rbp)
    1429:       48 8b 45 e8             mov    -0x18(%rbp),%rax
    142d:       8a 44 05 c2             mov    -0x3e(%rbp,%rax,1),%al
    1431:       88 45 be                mov    %al,-0x42(%rbp)
    1434:       48 8d 7d bc             lea    -0x44(%rbp),%rdi
    1438:       e8 53 fc ff ff          call   1090 <atoi@plt>
    143d:       88 c1                   mov    %al,%cl
    143f:       48 63 45 f4             movslq -0xc(%rbp),%rax
    1443:       88 4c 05 df             mov    %cl,-0x21(%rbp,%rax,1)
    1447:       48 8b 45 e8             mov    -0x18(%rbp),%rax
    144b:       48 83 c0 03             add    $0x3,%rax
    144f:       48 89 45 e8             mov    %rax,-0x18(%rbp)
    1453:       8b 45 f4                mov    -0xc(%rbp),%eax
    1456:       83 c0 01                add    $0x1,%eax
    1459:       89 45 f4                mov    %eax,-0xc(%rbp)
    145c:       e9 66 ff ff ff          jmp    13c7 <main+0xa7>
    1461:       48 63 45 f4             movslq -0xc(%rbp),%rax
    1465:       c6 44 05 df 00          movb   $0x0,-0x21(%rbp,%rax,1)
    146a:       48 8d 35 93 0b 00 00    lea    0xb93(%rip),%rsi        # 2004 <_IO_stdin_used+0x4>
    1471:       48 8d 7d df             lea    -0x21(%rbp),%rdi
    1475:       e8 f6 fb ff ff          call   1070 <strcmp@plt>
    147a:       89 45 f0                mov    %eax,-0x10(%rbp)
    147d:       8b 45 f0                mov    -0x10(%rbp),%eax
    1480:       89 45 ac                mov    %eax,-0x54(%rbp)
    1483:       83 e8 fe                sub    $0xfffffffe,%eax
    1486:       0f 84 aa 00 00 00       je     1536 <main+0x216>
    148c:       e9 00 00 00 00          jmp    1491 <main+0x171>
    1491:       8b 45 ac                mov    -0x54(%rbp),%eax
    1494:       83 e8 ff                sub    $0xffffffff,%eax
    1497:       0f 84 8f 00 00 00       je     152c <main+0x20c>
    149d:       e9 00 00 00 00          jmp    14a2 <main+0x182>
    14a2:       8b 45 ac                mov    -0x54(%rbp),%eax
    14a5:       85 c0                   test   %eax,%eax
    14a7:       0f 84 b1 00 00 00       je     155e <main+0x23e>
    14ad:       e9 00 00 00 00          jmp    14b2 <main+0x192>
    14b2:       8b 45 ac                mov    -0x54(%rbp),%eax
    14b5:       83 e8 01                sub    $0x1,%eax
    14b8:       0f 84 5a 00 00 00       je     1518 <main+0x1f8>
    14be:       e9 00 00 00 00          jmp    14c3 <main+0x1a3>
    14c3:       8b 45 ac                mov    -0x54(%rbp),%eax
    14c6:       83 e8 02                sub    $0x2,%eax
    14c9:       0f 84 53 00 00 00       je     1522 <main+0x202>
    14cf:       e9 00 00 00 00          jmp    14d4 <main+0x1b4>
    14d4:       8b 45 ac                mov    -0x54(%rbp),%eax
    14d7:       83 e8 03                sub    $0x3,%eax
    14da:       0f 84 60 00 00 00       je     1540 <main+0x220>
    14e0:       e9 00 00 00 00          jmp    14e5 <main+0x1c5>
    14e5:       8b 45 ac                mov    -0x54(%rbp),%eax
    14e8:       83 e8 04                sub    $0x4,%eax
    14eb:       0f 84 59 00 00 00       je     154a <main+0x22a>
    14f1:       e9 00 00 00 00          jmp    14f6 <main+0x1d6>
    14f6:       8b 45 ac                mov    -0x54(%rbp),%eax
    14f9:       83 e8 05                sub    $0x5,%eax
    14fc:       0f 84 52 00 00 00       je     1554 <main+0x234>
    1502:       e9 00 00 00 00          jmp    1507 <main+0x1e7>
    1507:       8b 45 ac                mov    -0x54(%rbp),%eax
    150a:       83 e8 73                sub    $0x73,%eax
    150d:       0f 84 55 00 00 00       je     1568 <main+0x248>
    1513:       e9 5a 00 00 00          jmp    1572 <main+0x252>
    1518:       e8 c3 fd ff ff          call   12e0 <___syscall_malloc>
    151d:       e9 55 00 00 00          jmp    1577 <main+0x257>
    1522:       e8 b9 fd ff ff          call   12e0 <___syscall_malloc>
    1527:       e9 4b 00 00 00          jmp    1577 <main+0x257>
    152c:       e8 af fd ff ff          call   12e0 <___syscall_malloc>
    1531:       e9 41 00 00 00          jmp    1577 <main+0x257>
    1536:       e8 a5 fd ff ff          call   12e0 <___syscall_malloc>
    153b:       e9 37 00 00 00          jmp    1577 <main+0x257>
    1540:       e8 9b fd ff ff          call   12e0 <___syscall_malloc>
    1545:       e9 2d 00 00 00          jmp    1577 <main+0x257>
    154a:       e8 91 fd ff ff          call   12e0 <___syscall_malloc>
    154f:       e9 23 00 00 00          jmp    1577 <main+0x257>
    1554:       e8 87 fd ff ff          call   12e0 <___syscall_malloc>
    1559:       e9 19 00 00 00          jmp    1577 <main+0x257>
    155e:       e8 9d fd ff ff          call   1300 <____syscall_malloc>
    1563:       e9 0f 00 00 00          jmp    1577 <main+0x257>
    1568:       e8 73 fd ff ff          call   12e0 <___syscall_malloc>
    156d:       e9 05 00 00 00          jmp    1577 <main+0x257>
    1572:       e8 69 fd ff ff          call   12e0 <___syscall_malloc>
    1577:       31 c0                   xor    %eax,%eax
    1579:       48 83 c4 60             add    $0x60,%rsp
    157d:       5d                      pop    %rbp
    157e:       c3                      ret    

Disassembly of section .fini:
```

when looking at the objdump of main, none of these custom functions are used and the structure looks kinda similar to level 2>
With a call to printf, a call to scanf, then a logic of loop with strlen and atoi and at the end a strcmp
We also see lots of call to a function ___syscall_malloc, which has no link whatsoever with the malloc function of the libc.

```bash
    00000000000012e0 <___syscall_malloc>:
    12e0:       55                      push   %rbp
    12e1:       48 89 e5                mov    %rsp,%rbp
    12e4:       48 8d 3d 48 0d 00 00    lea    0xd48(%rip),%rdi        # 2033 <_IO_stdin_used+0x33>
    12eb:       e8 40 fd ff ff          call   1030 <puts@plt>
    12f0:       bf 01 00 00 00          mov    $0x1,%edi
    12f5:       e8 b6 fd ff ff          call   10b0 <exit@plt>
    12fa:       66 0f 1f 44 00 00       nopw   0x0(%rax,%rax,1)
```

it is just a function that puts a message and exit (basically the no() function of level2)
We also see one call to a custom function "____syscall_malloc" (with 4 leading underscores not 3)

```bash
    0000000000001300 <____syscall_malloc>:
    1300:       55                      push   %rbp
    1301:       48 89 e5                mov    %rsp,%rbp
    1304:       48 8d 3d 2e 0d 00 00    lea    0xd2e(%rip),%rdi        # 2039 <_IO_stdin_used+0x39>
    130b:       e8 20 fd ff ff          call   1030 <puts@plt>
    1310:       5d                      pop    %rbp
    1311:       c3                      ret    
    1312:       66 2e 0f 1f 84 00 00    cs nopw 0x0(%rax,%rax,1)
    1319:       00 00 00 
    131c:       0f 1f 40 00             nopl   0x0(%rax)
```

which also displays a message but then return (must be the equivalent of the ok() function of level2)

Let's look at it with ghidra.
And indeed, the program has exactly the same logic than for level2, except that this time the password must begin by 42 and then must spell "*******" in ASCII decimal