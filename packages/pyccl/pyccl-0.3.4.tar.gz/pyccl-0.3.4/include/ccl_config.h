/** @file */
#ifdef __cplusplus
extern "C" {
#endif

#pragma once

/** 
 * Transfer function typedef.
 * Contains all information that describes a specific
 * transfer function. This includes whether there is an
 * emulator being used (Note: not implemented yet),
 * if there is a fitting function (E&H is the only option
 * right now), whether to use the BBKS transfer function,
 * and what boltzmann code to use.
 */
typedef enum transfer_function_t
{
  // If using an emulator for P_NL
  ccl_emulator          = 0,
  ccl_none              = 0,
  
  ccl_fitting_function  = 1,
  ccl_eisenstein_hu     = 1,
  
  ccl_bbks              = 2,

  ccl_boltzmann         = 3,
  ccl_boltzmann_class   = 3,
  
  ccl_boltzmann_camb    = 4,
  
} transfer_function_t;

/** 
 * Matter power spectrum typedef.
 * Contains all information that describes a specific
 * matter power spectrum. This inclues whether we
 * want the linear power spectrum, whether we use
 * halofit, and what halo model is being used.
 */
typedef enum matter_power_spectrum_t
{
    ccl_linear           = 0,

    ccl_halofit          = 1,
    // more?
    ccl_halo_model       = 3,
    // even more kinds ...
    ccl_emu              = 4
} matter_power_spectrum_t;

/** 
 * Bayrons power spectrum typedef.
 * Specified what model is being used for accounting
 * for the impact of baryonic processes on the total
 * matter power spectrum
 */
typedef enum baryons_power_spectrum_t
{
  ccl_nobaryons           = 0,
  
  ccl_bcm                 = 1
  // even more kinds ... 
} baryons_power_spectrum_t;

/** 
 * Mass function typedef
 * Contains all information that describes a specific
 * mass function. This is basically a switch that chooses
 * between Tinker08, Tinker10, Watson and Angulo mass
 * functions.
 */
typedef enum mass_function_t
{
  ccl_tinker      = 1,
  ccl_tinker10    = 2,
  ccl_watson      = 3,
  ccl_angulo      = 4
} mass_function_t;

/** 
 * Emulator neutrinos typedef
 * Specified whether, when the cosmic emulator is switched on,
 * CCL should exit if non-equal neutrino masses are passed (strict)
 * or equalize the masses, resulting in potential slight inconsistencies.
*/
typedef enum emulator_neutrinos_t
{
  ccl_emu_strict   = 1,
  ccl_emu_equalize = 2
} emulator_neutrinos_t;

/** 
 * Configuration typedef.
 * This contains the transfer function,
 * matter power spectrum, and mass function
 * that is being used currently.
 */
typedef struct ccl_configuration {
  transfer_function_t      transfer_function_method;
  matter_power_spectrum_t  matter_power_spectrum_method;
  baryons_power_spectrum_t  baryons_power_spectrum_method;
  mass_function_t          mass_function_method;
  emulator_neutrinos_t emulator_neutrinos_method;
  // TODO: Halo definition
} ccl_configuration;

/**
 * The default configuration object
 * In the default configuration, defined in ccl_core.c
 * CCL runs with:
 * default_config = {ccl_boltzmann_class, ccl_halofit, ccl_nobaryons, ccl_tinker10, ccl_emu_strict}
 */
extern const ccl_configuration default_config;

#ifdef __cplusplus
}
#endif
