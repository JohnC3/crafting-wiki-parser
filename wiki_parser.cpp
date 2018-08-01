#define AUSELESSMACRO 1

#include <iostream>
#include <fstream>
#include <cstdlib>

// ofstream: Stream class to write on files
// ifstream: Stream class to read from files
// fstream: Stream class that both writes to and reads from files

int main() {
  char * fpath = "/Users/jclements/Desktop/crafting-wiki-parser/example.html";

  std::cout << fpath << std::endl;
  printf("The value of AUSELESSMACRO is %d\n", AUSELESSMACRO);

  string line;
  ifstream file_stream;
  file_stream.open(fpath);

  if (file_stream.is_open()){
    printf("The file is open\n");
    while(getline(file_stream, line)){
      std::cout << line << '\n';
    }

  }

  file_stream.close();

  return 0;
}
