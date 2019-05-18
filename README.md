# Image Compression

## How It Works
    This uses fourier transforms. More specifically fast fourier transforms (FFT).
    FFT will bring the image to frequency space. To compress remove low frequencies and save the image. 
    To open/ show the filtered image, do the inverse FFT to bring the image back to the spatial domain.
    JPEG compression is more involved than this but as one of it's steps it uses a variant of FFT called
    Discrete Cosine Transform (DCT).

## Fast Fourier Transform
    This is a N Log N solution to converting a signal into its frequencies. Regular Fourier Transform takes N^2 time. 
    We rely on numpy fft library to acomplish this.

## Sources 
    Phenomenal Demo: http://madebyevan.com/dft/
    Image Processing and Fourier: https://homepages.inf.ed.ac.uk/rbf/HIPR2/fourier.html
    Gilbert Strang: https://ocw.mit.edu/courses/mathematics/18-085-computational-science-and-engineering-i-fall-2008/video-lectures/lecture-31-fast-fourier-transform-convolution/
