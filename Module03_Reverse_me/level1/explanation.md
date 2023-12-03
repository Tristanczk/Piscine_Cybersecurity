```bash
level1 git:(main) ✗ strings -d level1
/lib/ld-linux.so.2
"R9l    cj
_IO_stdin_used
__isoc99_scanf
__cxa_finalize
__libc_start_main
printf
strcmp
libc.so.6
GLIBC_2.7
GLIBC_2.1.3
GLIBC_2.34
GLIBC_2.0
_ITM_deregisterTMCloneTable
__gmon_start__
_ITM_registerTMCloneTable
__stack_check
Please enter key: 
Good job.
Nope.
;*2$"
```

```bash
level1 git:(main) ✗ nm level1 
000001cc r __abi_tag
00004024 B __bss_start
00004024 b completed.0
         w __cxa_finalize@GLIBC_2.1.3
0000401c D __data_start
0000401c W data_start
000010d0 t deregister_tm_clones
00001160 t __do_global_dtors_aux
00003ef8 d __do_global_dtors_aux_fini_array_entry
00004020 D __dso_handle
00003efc d _DYNAMIC
00004024 D _edata
00004028 B _end
0000127c T _fini
00002000 R _fp_hw
000011b0 t frame_dummy
00003ef4 d __frame_dummy_init_array_entry
000020f4 r __FRAME_END__
00004000 d _GLOBAL_OFFSET_TABLE_
         w __gmon_start__
00002040 r __GNU_EH_FRAME_HDR
00001000 T _init
00002004 R _IO_stdin_used
         U __isoc99_scanf@GLIBC_2.7
         w _ITM_deregisterTMCloneTable
         w _ITM_registerTMCloneTable
         U __libc_start_main@GLIBC_2.34
000011c0 T main
         U printf@GLIBC_2.0
00001110 t register_tm_clones
00001090 T _start
         U strcmp@GLIBC_2.0
00004024 D __TMC_END__
000010c0 T __x86.get_pc_thunk.bx
000011b9 T __x86.get_pc_thunk.dx
```

When looking at the program functions in main, we see that the program uses printf and strcmp from the libc.
When we look at the strings, we see 3 strings of interest:
Please enter key: 
Good job.
Nope.

We can suppose that the program is prompting the user for a key (through the scanf call), then must likely compare the key to a value and print the according response.
The goal here will be to identify the value that is used in the strcmp function.


```bash
Dump of assembler code for function main:
   0x565561c0 <+0>:     push   %ebp
   0x565561c1 <+1>:     mov    %esp,%ebp
   0x565561c3 <+3>:     push   %ebx
=> 0x565561c4 <+4>:     sub    $0x84,%esp
   0x565561ca <+10>:    call   0x565561cf <main+15>
   0x565561cf <+15>:    pop    %ebx
   0x565561d0 <+16>:    add    $0x2e31,%ebx
   0x565561d6 <+22>:    mov    %ebx,-0x80(%ebp)
   0x565561d9 <+25>:    movl   $0x0,-0x8(%ebp)
   0x565561e0 <+32>:    mov    -0x1ff8(%ebx),%eax
   0x565561e6 <+38>:    mov    %eax,-0x7a(%ebp)
   0x565561e9 <+41>:    mov    -0x1ff4(%ebx),%eax
   0x565561ef <+47>:    mov    %eax,-0x76(%ebp)
   0x565561f2 <+50>:    mov    -0x1ff0(%ebx),%eax
   0x565561f8 <+56>:    mov    %eax,-0x72(%ebp)
   0x565561fb <+59>:    mov    -0x1fec(%ebx),%ax
   0x56556202 <+66>:    mov    %ax,-0x6e(%ebp)
   0x56556206 <+70>:    lea    -0x1fea(%ebx),%eax
   0x5655620c <+76>:    mov    %eax,(%esp)
   0x5655620f <+79>:    call   0x56556060 <printf@plt>
   0x56556214 <+84>:    mov    -0x80(%ebp),%ebx
   0x56556217 <+87>:    lea    -0x6c(%ebp),%eax
   0x5655621a <+90>:    lea    -0x1fd7(%ebx),%ecx
   0x56556220 <+96>:    mov    %ecx,(%esp)
   0x56556223 <+99>:    mov    %eax,0x4(%esp)
   0x56556227 <+103>:   call   0x56556070 <__isoc99_scanf@plt>
   0x5655622c <+108>:   mov    -0x80(%ebp),%ebx
   0x5655622f <+111>:   lea    -0x6c(%ebp),%ecx
   0x56556232 <+114>:   lea    -0x7a(%ebp),%edx
   0x56556235 <+117>:   mov    %esp,%eax
   0x56556237 <+119>:   mov    %edx,0x4(%eax)
   0x5655623a <+122>:   mov    %ecx,(%eax)
   0x5655623c <+124>:   call   0x56556040 <strcmp@plt>
   0x56556241 <+129>:   cmp    $0x0,%eax
   0x56556244 <+132>:   jne    0x56556260 <main+160>
   0x5655624a <+138>:   mov    -0x80(%ebp),%ebx
   0x5655624d <+141>:   lea    -0x1fd4(%ebx),%eax
   0x56556253 <+147>:   mov    %eax,(%esp)
   0x56556256 <+150>:   call   0x56556060 <printf@plt>
   0x5655625b <+155>:   jmp    0x56556271 <main+177>
   0x56556260 <+160>:   mov    -0x80(%ebp),%ebx
   0x56556263 <+163>:   lea    -0x1fc9(%ebx),%eax
   0x56556269 <+169>:   mov    %eax,(%esp)
   0x5655626c <+172>:   call   0x56556060 <printf@plt>
   0x56556271 <+177>:   xor    %eax,%eax
   0x56556273 <+179>:   add    $0x84,%esp
   0x56556279 <+185>:   pop    %ebx
   0x5655627a <+186>:   pop    %ebp
   0x5655627b <+187>:   ret    
End of assembler dump.
```

when we look at the assembler dump of main, we see that the program first calls printf (printing the prompt : "Please enter key: ")
then it gets user input using scanf
then it will compare the user input with a string and if the result is equal to 0, print "Good job." and if the result is different than 0 (strings not equal), it will print "Nope."
We can then set a breakpoint before the call to strcmp break *0x5655623a and run our program that will prompt us for a password (for instance "bonjour")
then at the strcmp breakpoint, we can inspect the registers:
```bash
(gdb) x/s $ecx
0xffffc96c:     "bonjour"
(gdb) x/s $edx
0xffffc95e:     "__stack_check"
```
ecx and edx contains the 2 strcmp arguments, ecx is our proposal and edx is what it is compared to, bingo !