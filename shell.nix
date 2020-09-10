with import <nixpkgs> {};
mkShell {
  buildInputs = [
    python37
    python37Packages.pyserial
    python37Packages.prompt_toolkit
    python37Packages.pyyaml
  ];
}
