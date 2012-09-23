#!/bin/bash
# script to generate transverse slices of dummy diffusion experiments

# source constants.sh relative to this file

. $( cd "$( dirname "$0" )" && pwd )/init.sh

generate_noisy_slice() {
  # build arguments
  ITERATION=$1
  VOLUME_PATH=results/dummy/200_alpha0.4rt/HiResPairs/AdjustedTransforms/CenteredAffineTransform_$ITERATION/HiRes_colour.mha
  TIFF_PATH=2_methods/Figs/0450.tiff
  PDF_PATH=2_methods/Figs/cross_section_${ITERATION}.pdf
  
  # generate slices
  extract_slice $VOLUME_PATH 2_methods/Figs 0 0450
  flip_and_convert_slice $TIFF_PATH $PDF_PATH
}

generate_perfect_slice() {
  # build arguments
  VOLUME_PATH=results/dummy/perfect_200_alpha0.4rt/HiResTransforms_1_8/CenteredAffineTransform/HiRes_colour.mha
  TIFF_PATH=2_methods/Figs/0450.tiff
  PDF_PATH=2_methods/Figs/cross_section_perfect.pdf
  
  # generate slices
  extract_slice $VOLUME_PATH 2_methods/Figs 0 0450
  flip_and_convert_slice $TIFF_PATH $PDF_PATH
}

# generate noisy slices
for iteration in 0 1 7 40; do
  echo iteration: $iteration
  generate_noisy_slice $iteration
  echo
done

# # generate perfect slices
echo perfect slice
generate_perfect_slice
echo
