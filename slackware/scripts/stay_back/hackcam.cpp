#include <fcntl.h>
#include <unistd.h>
#include <sys/ioctl.h>
#include <linux/videodev2.h>
#include <sys/mman.h>
#include <cstring>
#include <cstdio>

struct Buffer {
    void* start;
    size_t length;
};

int main() {
    const char* dev_name = "/dev/video0";
    int fd = open(dev_name, O_RDWR);
    if (fd < 0) return 1;

    v4l2_capability caps;
    if (ioctl(fd, VIDIOC_QUERYCAP, &caps) < 0) {
        close(fd);
        return 1;
    }

    if (!(caps.capabilities & V4L2_CAP_VIDEO_CAPTURE) || !(caps.capabilities & V4L2_CAP_STREAMING)) {
        close(fd);
        return 1;
    }

    v4l2_format fmt;
    memset(&fmt, 0, sizeof(fmt));
    fmt.type = V4L2_BUF_TYPE_VIDEO_CAPTURE;
    fmt.fmt.pix.width = 320;
    fmt.fmt.pix.height = 240;
    fmt.fmt.pix.pixelformat = V4L2_PIX_FMT_YUYV;
    fmt.fmt.pix.field = V4L2_FIELD_NONE;

    if (ioctl(fd, VIDIOC_S_FMT, &fmt) < 0) {
        close(fd);
        return 1;
    }

    v4l2_requestbuffers req;
    memset(&req, 0, sizeof(req));
    req.count = 1;
    req.type = V4L2_BUF_TYPE_VIDEO_CAPTURE;
    req.memory = V4L2_MEMORY_MMAP;

    if (ioctl(fd, VIDIOC_REQBUFS, &req) < 0) {
        close(fd);
        return 1;
    }

    Buffer buffer;
    v4l2_buffer buf;
    memset(&buf, 0, sizeof(buf));
    buf.type = V4L2_BUF_TYPE_VIDEO_CAPTURE;
    buf.memory = V4L2_MEMORY_MMAP;
    buf.index = 0;

    if (ioctl(fd, VIDIOC_QUERYBUF, &buf) < 0) {
        close(fd);
        return 1;
    }

    buffer.length = buf.length;
    buffer.start = mmap(NULL, buf.length, PROT_READ | PROT_WRITE, MAP_SHARED, fd, buf.m.offset);
    if (buffer.start == MAP_FAILED) {
        close(fd);
        return 1;
    }

    if (ioctl(fd, VIDIOC_QBUF, &buf) < 0) {
        munmap(buffer.start, buffer.length);
        close(fd);
        return 1;
    }

    v4l2_buf_type type = V4L2_BUF_TYPE_VIDEO_CAPTURE;
    if (ioctl(fd, VIDIOC_STREAMON, &type) < 0) {
        munmap(buffer.start, buffer.length);
        close(fd);
        return 1;
    }

    if (ioctl(fd, VIDIOC_DQBUF, &buf) < 0) {
        ioctl(fd, VIDIOC_STREAMOFF, &type);
        munmap(buffer.start, buffer.length);
        close(fd);
        return 1;
    }

    int width = fmt.fmt.pix.width;
    int height = fmt.fmt.pix.height;
    unsigned char* yuyv = (unsigned char*)buffer.start;

    FILE* f = fopen("photo.pgm", "wb");
    if (!f) {
        ioctl(fd, VIDIOC_STREAMOFF, &type);
        munmap(buffer.start, buffer.length);
        close(fd);
        return 1;
    }

    fprintf(f, "P5\n%d %d\n255\n", width, height);
    for (int i = 0; i < width * height; i++) {
        unsigned char y = yuyv[i * 2];
        fwrite(&y, 1, 1, f);
    }
    fclose(f);

    ioctl(fd, VIDIOC_STREAMOFF, &type);
    munmap(buffer.start, buffer.length);
    close(fd);

    return 0;
}
