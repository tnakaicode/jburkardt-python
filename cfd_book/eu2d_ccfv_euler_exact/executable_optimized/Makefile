##########################################################
# Makefile for EDU2D-CCFV-Euler-EXPLCT
##########################################################
 PROGRAM = edu2d
##########################################################
# Suffix Rule for f90
# Note: use "gfortran -O2" for best performance, but
#       don't use it until you're sure bugs are removed.
##########################################################
.SUFFIXES : .o .f90
.f90.o:
	gfortran -O2 -c $<
##########################################################
SDIR = ../src_files
OBCTS =	$(SDIR)/edu2d_module_input_parameter.o\
	$(SDIR)/edu2d_module_mms.o\
	$(SDIR)/edu2d_module_common_data.o\
	$(SDIR)/edu2d_module_ccfv_data_grid.o\
	$(SDIR)/edu2d_module_ccfv_data_soln.o\
	$(SDIR)/edu2d_module_write_files.o\
	$(SDIR)/edu2d_module_ccfv_gradient.o\
	$(SDIR)/edu2d_module_flux.o\
	$(SDIR)/edu2d_module_bc_states.o\
	$(SDIR)/edu2d_module_ccfv_limiter.o\
	$(SDIR)/edu2d_module_ccfv_residual.o\
	$(SDIR)/edu2d_module_explicit_solver.o\
	$(SDIR)/edu2d_main.o\
##########################################################
# Make executable "mg"
# Note: use "gfortran -O2" for best performance, but
#       don't use it until you're sure bugs are removed.
##########################################################
$(PROGRAM): $(OBCTS)
	gfortran -O2 -o $@ $(OBCTS)
#
SDIR = .
##########################################################
# Clean up
##########################################################
clean:
	rm -f *.o
	rm -f *.mod
	rm -f edu2d
