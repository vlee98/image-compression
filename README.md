# Image Compression (JPEG Variant)

## How It Works
    This uses fourier transforms. More specifically fast fourier transforms (FFT).
    JPEG typically uses Discrete Cosine Transform, a variant of FFT. 
    FFT will bring the image to frequency space. To compress remove low frequencies and save the image. 
    To open/ show the filtered image, do the inverse FFT to bring the image back to the spatial domain.

## Fast Fourier Transform

## Sources 
