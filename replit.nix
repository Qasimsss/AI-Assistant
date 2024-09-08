{ pkgs }: {
  deps = [
    pkgs.espeak-ng
    pkgs.glibcLocales
    pkgs.libxcrypt
    pkgs.cacert
    pkgs.python310Full
    pkgs.espeak
    pkgs.portaudio
  ];
}
