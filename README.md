# Image Compression

## How It Works & Analysis
    This uses fourier transforms. More specifically fast fourier transforms (FFT).
    FFT will bring the image to frequency space. To compress remove low frequencies. 
    Then do the inverse FFT to bring the image back to the spatial domain. 
    This relies on the compression done by the skimage io.imsave function which will compress the image further due to 
    the 0 value pixels. At .0001 compression the rose image moves from 1014917 Bytes to 451519 Bytes.
    The major part of JPEG compression is a variant of FFT called Discrete Cosine Transform (DCT).
    JPEG compression from scratch would involve cropping, segmenting, etc. but the major lesson learned was the frequency vs spatial domain.

## Fast Fourier Transform
    This is a N Log N solution to converting a signal into its frequencies. Regular Fourier Transform takes N^2 time. 
    We rely on numpy fft library to acomplish this.

## Sources 
    Phenomenal Demo: http://madebyevan.com/dft/
    Image Processing and Fourier: https://homepages.inf.ed.ac.uk/rbf/HIPR2/fourier.html
    Gilbert Strang: https://ocw.mit.edu/courses/mathematics/18-085-computational-science-and-engineering-i-fall-2008/video-lectures/lecture-31-fast-fourier-transform-convolution/
