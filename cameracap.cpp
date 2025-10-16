#include <cstdlib>

int main(){
    system("ffmpeg -f v4l2 -i /dev/video0 -frames:v 1 output.jpg");
    system("bash i2s.sh");
    return 0;
}