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
	return fmt.Sprintf("File{name:%s, size:%d, parent:%s}\n", f.name, f.size, f.parent)
}

func (d *Directory) String() string {
	return fmt.Sprintf("Directory{name:%s, parent:%s, childDirectories:%s, files:%v}\n", d.name, d.parent, d.childDirectories, d.files)
}

type FileSystem map[string]*Directory

func cd(directoryName string, currentDir string, fileSystem FileSystem) string {
	if directoryName == ".." {
		currentDir = fileSystem[currentDir].parent
	} else {
		currentDir = directoryName
	}
	return currentDir
}

func dir(directoryName string, currentDir string, fileSystem FileSystem) {
	fileSystem[directoryName] = &Directory{name: directoryName, parent: currentDir, size: 0, files: []File{}, childDirectories: []string{}}
	fileSystem[currentDir].childDirectories = append(fileSystem[currentDir].childDirectories, directoryName)
}

func addFile(fileName string, fileSize string, currentDir string, fileSystem FileSystem) {
	fileSizeInt, _ := strconv.Atoi(fileSize)
	fileSystem[currentDir].files = append(fileSystem[currentDir].files, File{name: fileName, size: fileSizeInt})
	fileSystem[currentDir].size += fileSizeInt
}

//func ls(currentDir string, fileSystem FileSystem) {
//	fmt.Println("here")
//	for _, file := range fileSystem[currentDir].files {
//		fmt.Printf("%d %s\n", file.size, file.name)
//	}
//	for _, directory := range fileSystem[currentDir].childDirectories {
//		fmt.Printf("dir %s\n", directory)
//	}
//}

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
	currentDir := "/"
	fileSystem := FileSystem{"/": &Directory{name: "/", parent: "/", size: 0, files: []File{}, childDirectories: []string{}}}

	for scanner.Scan() {
		command := scanner.Text()
		split := strings.Split(command, " ")
		if string(split[0]) == "$" {
			if split[1] == "cd" {
				currentDir = cd(split[2], currentDir, fileSystem)
			}
		} else if string(split[0]) == "dir" {
			dir(split[1], currentDir, fileSystem)
		} else {
			addFile(split[1], split[0], currentDir, fileSystem)
		}
	}
	fmt.Println(fileSystem)

	totalSize := 0

	for _, directory := range fileSystem {
		size := computeSize(directory, fileSystem)

		if size <= 100000 {
			fmt.Println(directory.name, size)
			totalSize += size
		}
	}
	// 1089720 is low
	fmt.Println(totalSize)
}
