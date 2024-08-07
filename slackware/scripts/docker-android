#!/bin/bash

# android-container Copyright 2023 budi utomo
# https://github.com/budtmo/docker-android/blob/master/LICENSE.md
# https://github.com/budtmo/docker-android/blob/master/documentations/USER_BEHAVIOR_ANALYTICS.md

# This script LICENSE is MIT 
# https://opensource.org/license/mit
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED 
# TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# Check Docker status
status_output=$(/etc/rc.d/rc.docker status)

# Check if Docker is running
if echo "$status_output" | grep -q "Status of dockerd: running"; then
    echo "Docker is running."
    docker run -d -p 6080:6080 -e EMULATOR_DEVICE="Samsung Galaxy S10" -e WEB_VNC=true --device /dev/kvm --name android-container budtmo/docker-android:emulator_14.0
    xdg-open http://localhost:6080/
else
    echo "Docker is not running."
    # Perform actions when Docker is not running
    echo "Please as root command:"
    echo "/etc/rc.d/rc.docker start"
    echo "And run again this script."
    exit
fi

