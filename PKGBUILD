pkgname=faba-colors-git
_pkgname=faba-colors
pkgver=2.0
pkgrel=1
pkgdesc="These are supplementary theme for the Faba icon set. It contains colourified versions of the Faba icons."
arch=('any')
url="https://github.com/snwh/faba-colors"
license=('GPL3')
depends=('faba-icons-git')
makedepends=('git')
optdepends=()
provides=('faba-colors-git')
conflicts=('faba-colors-git')
source=('git+https://github.com/snwh/faba-colors.git')
md5sums=('SKIP')

pkgver() {
  cd $srcdir/$_pkgname
  echo $(git rev-list --count HEAD).$(git rev-parse --short HEAD)
}

package() {

  # create theme dirs
  install -d -m 755 "$pkgdir"/usr/share/icons/Faba-Ceru
  install -d -m 755 "$pkgdir"/usr/share/icons/Faba-Lutu
  install -d -m 755 "$pkgdir"/usr/share/icons/Faba-Roja
  install -d -m 755 "$pkgdir"/usr/share/icons/Faba-Verd

  # install theme
  cd $srcdir/faba-colors/Faba-Ceru
  cp -r . "$pkgdir"/usr/share/icons/Faba-Ceru/
  cd $srcdir/faba-colors/Faba-Lutu
  cp -r . "$pkgdir"/usr/share/icons/Faba-Lutu/
  cd $srcdir/faba-colors/Faba-Roja
  cp -r . "$pkgdir"/usr/share/icons/Faba-Roja/
  cd $srcdir/faba-colors/Faba-Verd
  cp -r . "$pkgdir"/usr/share/icons/Faba-Verd/
}
