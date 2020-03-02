##########################################################
# Makefile for EDU2D-Template:
#
# Note: I don't know much about Makefile.
#       You can ask questions but please don't expect
#       good answers. Thank you for your understanding!
#
# Written by Katate Masatsuka, http://www.cfdbooks.com
##########################################################
 PROGRAM = edu2d_template
##########################################################
# Suffix Rule for f90
##########################################################
.SUFFIXES : .o .f90
.f90.o:
	gfortran -O2 -c $<
##########################################################
SDIR = .
OBCTS =	$(SDIR)/edu2d_basic_package_v0.o\
	$(SDIR)/edu2d_template_nc_v0.o\
	$(SDIR)/edu2d_template_cc_v0.o\
	$(SDIR)/edu2d_template_main_v0.o\
##########################################################
# Make executable "edu2d_template"
##########################################################
$(PROGRAM): $(OBCTS)
	gfortran -O2 -o $@ $(OBCTS)
##########################################################
# Clean up: Type 'make clean'
##########################################################
clean:
	rm -f *.o
	rm -f *.mod
	rm -f *.M
##########################################################
# Clean up: Type 'make clean~'
##########################################################
clean~:
	rm -f *~
