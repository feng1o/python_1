project(server)
cmake_minimum_required(VERSION 2.6)

# INCLUDE_DIRECTORIES(${PROJECT_SOURCE_DIR}/include)
# link_directories(${PROJECT_SOURCE_DIR}/lib) 

message( STATUS "sources path " ${PROJECT_SOURCE_DIR})
message("......\n")

SET(CMAKE_VERBOSE_MAKEFILE on)

aux_source_directory(. dir_srcs)
add_executable(server ${dir_srcs})
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g -O0  -lpthread") # 参数
# set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g -O0 -lpthread")
                                                                                                 
set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/build/)
target_link_libraries(server pthread)
