# cgc_loader

A modified version of IDA CGC Loader Module from idabook.com

Original link: http://idabook.com/cgc/cgc_ldr.tgz

---
Rebuild til and add base function F.L.I.R.T support.

Use `tilib -c -hlibcgc.h -hlibpov.h -Ccg -v -t"Default CGC Type Library" cgc.til` to create new til file.

Use ```ar qc test.a `pypy cgc2elf.py .` ```to create a library named test.a that contains complied function and symbols.

Use ```pelf -v test.a libcgc_sample.pat``` to create pat files.

Use ```sigmake -n"CGC Libc Collection" -lr__Z `ls *.pat` cgc_libc.sig``` to make F.L.I.R.T signature from prepared pat files.
