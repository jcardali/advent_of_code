package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type File struct {
	name   string
	size   int
	parent string
}

type Directory struct {
	name             string
	parent           string
	size             int
	files            []File
	childDirectories []string
}

func (f *File) String() string {
	return fmt.Sprintf("File{name:%s, size:%d, parent:%s}", f.name, f.size, f.parent)
}

func (d *Directory) String() string {
	return fmt.Sprintf("Directory{name:%s, parent:%s, childDirectories:%s, files:%v}", d.name, d.parent, d.childDirectories, d.files)
}

type FileSystem map[string]*Directory

func cd(directoryName string, currentPath []string) []string {
	if directoryName == ".." {
		return currentPath[:len(currentPath)-1]
	} else {
		return append(currentPath, directoryName)
	}
}

func dir(directoryName string, currentPath []string, fileSystem FileSystem) {
	oldPath := strings.Join(currentPath, "/")
	path := strings.Join(append(currentPath, directoryName), "/")
	fileSystem[path] = &Directory{name: directoryName, parent: currentPath[len(currentPath)-1], size: 0, files: []File{}, childDirectories: []string{}}
	fileSystem[oldPath].childDirectories = append(fileSystem[oldPath].childDirectories, path)
}

func addFile(fileName string, fileSize string, currentPath []string, fileSystem FileSystem) {
	path := strings.Join(currentPath, "/")
	fileSizeInt, _ := strconv.Atoi(fileSize)
	fileSystem[path].files = append(fileSystem[path].files, File{name: fileName, size: fileSizeInt})
	fileSystem[path].size += fileSizeInt
}

func computeSize(directory *Directory, fileSystem FileSystem) int {
	size := directory.size

	for _, child := range directory.childDirectories {
		size += computeSize(fileSystem[child], fileSystem)
	}

	return size
}

func main() {
	f, _ := os.Open("input.txt")

	defer f.Close()

	scanner := bufio.NewScanner(f)
	currentPath := []string{}
	fileSystem := FileSystem{"/": &Directory{name: "/", parent: "/", size: 0, files: []File{}, childDirectories: []string{}}}

	for scanner.Scan() {
		command := scanner.Text()
		split := strings.Split(command, " ")
		if string(split[0]) == "$" {
			if split[1] == "cd" {
				currentPath = cd(split[2], currentPath)
			}
		} else if string(split[0]) == "dir" {
			dir(split[1], currentPath, fileSystem)
		} else {
			addFile(split[1], split[0], currentPath, fileSystem)
		}
	}

	totalSize := 0

	for _, directory := range fileSystem {
		size := computeSize(directory, fileSystem)

		if size <= 100000 {
			totalSize += size
		}
	}
	fmt.Println(totalSize)
}
