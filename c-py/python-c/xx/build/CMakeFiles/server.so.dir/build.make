# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.4

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Produce verbose output by default.
VERBOSE = 1

# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/local/bin/cmake

# The command to remove a file.
RM = /usr/local/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/python_1/c-py/python-c/xx

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/python_1/c-py/python-c/xx/build

# Include any dependencies generated for this target.
include CMakeFiles/server.so.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/server.so.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/server.so.dir/flags.make

CMakeFiles/server.so.dir/rw_data.cpp.o: CMakeFiles/server.so.dir/flags.make
CMakeFiles/server.so.dir/rw_data.cpp.o: ../rw_data.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/python_1/c-py/python-c/xx/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/server.so.dir/rw_data.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/server.so.dir/rw_data.cpp.o -c /home/python_1/c-py/python-c/xx/rw_data.cpp

CMakeFiles/server.so.dir/rw_data.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/server.so.dir/rw_data.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/python_1/c-py/python-c/xx/rw_data.cpp > CMakeFiles/server.so.dir/rw_data.cpp.i

CMakeFiles/server.so.dir/rw_data.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/server.so.dir/rw_data.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/python_1/c-py/python-c/xx/rw_data.cpp -o CMakeFiles/server.so.dir/rw_data.cpp.s

CMakeFiles/server.so.dir/rw_data.cpp.o.requires:

.PHONY : CMakeFiles/server.so.dir/rw_data.cpp.o.requires

CMakeFiles/server.so.dir/rw_data.cpp.o.provides: CMakeFiles/server.so.dir/rw_data.cpp.o.requires
	$(MAKE) -f CMakeFiles/server.so.dir/build.make CMakeFiles/server.so.dir/rw_data.cpp.o.provides.build
.PHONY : CMakeFiles/server.so.dir/rw_data.cpp.o.provides

CMakeFiles/server.so.dir/rw_data.cpp.o.provides.build: CMakeFiles/server.so.dir/rw_data.cpp.o


CMakeFiles/server.so.dir/message.cpp.o: CMakeFiles/server.so.dir/flags.make
CMakeFiles/server.so.dir/message.cpp.o: ../message.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/python_1/c-py/python-c/xx/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/server.so.dir/message.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/server.so.dir/message.cpp.o -c /home/python_1/c-py/python-c/xx/message.cpp

CMakeFiles/server.so.dir/message.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/server.so.dir/message.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/python_1/c-py/python-c/xx/message.cpp > CMakeFiles/server.so.dir/message.cpp.i

CMakeFiles/server.so.dir/message.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/server.so.dir/message.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/python_1/c-py/python-c/xx/message.cpp -o CMakeFiles/server.so.dir/message.cpp.s

CMakeFiles/server.so.dir/message.cpp.o.requires:

.PHONY : CMakeFiles/server.so.dir/message.cpp.o.requires

CMakeFiles/server.so.dir/message.cpp.o.provides: CMakeFiles/server.so.dir/message.cpp.o.requires
	$(MAKE) -f CMakeFiles/server.so.dir/build.make CMakeFiles/server.so.dir/message.cpp.o.provides.build
.PHONY : CMakeFiles/server.so.dir/message.cpp.o.provides

CMakeFiles/server.so.dir/message.cpp.o.provides.build: CMakeFiles/server.so.dir/message.cpp.o


CMakeFiles/server.so.dir/tcp_listen.cpp.o: CMakeFiles/server.so.dir/flags.make
CMakeFiles/server.so.dir/tcp_listen.cpp.o: ../tcp_listen.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/python_1/c-py/python-c/xx/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object CMakeFiles/server.so.dir/tcp_listen.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/server.so.dir/tcp_listen.cpp.o -c /home/python_1/c-py/python-c/xx/tcp_listen.cpp

CMakeFiles/server.so.dir/tcp_listen.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/server.so.dir/tcp_listen.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/python_1/c-py/python-c/xx/tcp_listen.cpp > CMakeFiles/server.so.dir/tcp_listen.cpp.i

CMakeFiles/server.so.dir/tcp_listen.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/server.so.dir/tcp_listen.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/python_1/c-py/python-c/xx/tcp_listen.cpp -o CMakeFiles/server.so.dir/tcp_listen.cpp.s

CMakeFiles/server.so.dir/tcp_listen.cpp.o.requires:

.PHONY : CMakeFiles/server.so.dir/tcp_listen.cpp.o.requires

CMakeFiles/server.so.dir/tcp_listen.cpp.o.provides: CMakeFiles/server.so.dir/tcp_listen.cpp.o.requires
	$(MAKE) -f CMakeFiles/server.so.dir/build.make CMakeFiles/server.so.dir/tcp_listen.cpp.o.provides.build
.PHONY : CMakeFiles/server.so.dir/tcp_listen.cpp.o.provides

CMakeFiles/server.so.dir/tcp_listen.cpp.o.provides.build: CMakeFiles/server.so.dir/tcp_listen.cpp.o


CMakeFiles/server.so.dir/threadpoll.cpp.o: CMakeFiles/server.so.dir/flags.make
CMakeFiles/server.so.dir/threadpoll.cpp.o: ../threadpoll.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/python_1/c-py/python-c/xx/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building CXX object CMakeFiles/server.so.dir/threadpoll.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/server.so.dir/threadpoll.cpp.o -c /home/python_1/c-py/python-c/xx/threadpoll.cpp

CMakeFiles/server.so.dir/threadpoll.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/server.so.dir/threadpoll.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/python_1/c-py/python-c/xx/threadpoll.cpp > CMakeFiles/server.so.dir/threadpoll.cpp.i

CMakeFiles/server.so.dir/threadpoll.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/server.so.dir/threadpoll.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/python_1/c-py/python-c/xx/threadpoll.cpp -o CMakeFiles/server.so.dir/threadpoll.cpp.s

CMakeFiles/server.so.dir/threadpoll.cpp.o.requires:

.PHONY : CMakeFiles/server.so.dir/threadpoll.cpp.o.requires

CMakeFiles/server.so.dir/threadpoll.cpp.o.provides: CMakeFiles/server.so.dir/threadpoll.cpp.o.requires
	$(MAKE) -f CMakeFiles/server.so.dir/build.make CMakeFiles/server.so.dir/threadpoll.cpp.o.provides.build
.PHONY : CMakeFiles/server.so.dir/threadpoll.cpp.o.provides

CMakeFiles/server.so.dir/threadpoll.cpp.o.provides.build: CMakeFiles/server.so.dir/threadpoll.cpp.o


CMakeFiles/server.so.dir/main.cpp.o: CMakeFiles/server.so.dir/flags.make
CMakeFiles/server.so.dir/main.cpp.o: ../main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/python_1/c-py/python-c/xx/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Building CXX object CMakeFiles/server.so.dir/main.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/server.so.dir/main.cpp.o -c /home/python_1/c-py/python-c/xx/main.cpp

CMakeFiles/server.so.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/server.so.dir/main.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/python_1/c-py/python-c/xx/main.cpp > CMakeFiles/server.so.dir/main.cpp.i

CMakeFiles/server.so.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/server.so.dir/main.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/python_1/c-py/python-c/xx/main.cpp -o CMakeFiles/server.so.dir/main.cpp.s

CMakeFiles/server.so.dir/main.cpp.o.requires:

.PHONY : CMakeFiles/server.so.dir/main.cpp.o.requires

CMakeFiles/server.so.dir/main.cpp.o.provides: CMakeFiles/server.so.dir/main.cpp.o.requires
	$(MAKE) -f CMakeFiles/server.so.dir/build.make CMakeFiles/server.so.dir/main.cpp.o.provides.build
.PHONY : CMakeFiles/server.so.dir/main.cpp.o.provides

CMakeFiles/server.so.dir/main.cpp.o.provides.build: CMakeFiles/server.so.dir/main.cpp.o


CMakeFiles/server.so.dir/error.cpp.o: CMakeFiles/server.so.dir/flags.make
CMakeFiles/server.so.dir/error.cpp.o: ../error.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/python_1/c-py/python-c/xx/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_6) "Building CXX object CMakeFiles/server.so.dir/error.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/server.so.dir/error.cpp.o -c /home/python_1/c-py/python-c/xx/error.cpp

CMakeFiles/server.so.dir/error.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/server.so.dir/error.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/python_1/c-py/python-c/xx/error.cpp > CMakeFiles/server.so.dir/error.cpp.i

CMakeFiles/server.so.dir/error.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/server.so.dir/error.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/python_1/c-py/python-c/xx/error.cpp -o CMakeFiles/server.so.dir/error.cpp.s

CMakeFiles/server.so.dir/error.cpp.o.requires:

.PHONY : CMakeFiles/server.so.dir/error.cpp.o.requires

CMakeFiles/server.so.dir/error.cpp.o.provides: CMakeFiles/server.so.dir/error.cpp.o.requires
	$(MAKE) -f CMakeFiles/server.so.dir/build.make CMakeFiles/server.so.dir/error.cpp.o.provides.build
.PHONY : CMakeFiles/server.so.dir/error.cpp.o.provides

CMakeFiles/server.so.dir/error.cpp.o.provides.build: CMakeFiles/server.so.dir/error.cpp.o


# Object files for target server.so
server_so_OBJECTS = \
"CMakeFiles/server.so.dir/rw_data.cpp.o" \
"CMakeFiles/server.so.dir/message.cpp.o" \
"CMakeFiles/server.so.dir/tcp_listen.cpp.o" \
"CMakeFiles/server.so.dir/threadpoll.cpp.o" \
"CMakeFiles/server.so.dir/main.cpp.o" \
"CMakeFiles/server.so.dir/error.cpp.o"

# External object files for target server.so
server_so_EXTERNAL_OBJECTS =

server.so: CMakeFiles/server.so.dir/rw_data.cpp.o
server.so: CMakeFiles/server.so.dir/message.cpp.o
server.so: CMakeFiles/server.so.dir/tcp_listen.cpp.o
server.so: CMakeFiles/server.so.dir/threadpoll.cpp.o
server.so: CMakeFiles/server.so.dir/main.cpp.o
server.so: CMakeFiles/server.so.dir/error.cpp.o
server.so: CMakeFiles/server.so.dir/build.make
server.so: CMakeFiles/server.so.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/python_1/c-py/python-c/xx/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_7) "Linking CXX executable server.so"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/server.so.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/server.so.dir/build: server.so

.PHONY : CMakeFiles/server.so.dir/build

CMakeFiles/server.so.dir/requires: CMakeFiles/server.so.dir/rw_data.cpp.o.requires
CMakeFiles/server.so.dir/requires: CMakeFiles/server.so.dir/message.cpp.o.requires
CMakeFiles/server.so.dir/requires: CMakeFiles/server.so.dir/tcp_listen.cpp.o.requires
CMakeFiles/server.so.dir/requires: CMakeFiles/server.so.dir/threadpoll.cpp.o.requires
CMakeFiles/server.so.dir/requires: CMakeFiles/server.so.dir/main.cpp.o.requires
CMakeFiles/server.so.dir/requires: CMakeFiles/server.so.dir/error.cpp.o.requires

.PHONY : CMakeFiles/server.so.dir/requires

CMakeFiles/server.so.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/server.so.dir/cmake_clean.cmake
.PHONY : CMakeFiles/server.so.dir/clean

CMakeFiles/server.so.dir/depend:
	cd /home/python_1/c-py/python-c/xx/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/python_1/c-py/python-c/xx /home/python_1/c-py/python-c/xx /home/python_1/c-py/python-c/xx/build /home/python_1/c-py/python-c/xx/build /home/python_1/c-py/python-c/xx/build/CMakeFiles/server.so.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/server.so.dir/depend

