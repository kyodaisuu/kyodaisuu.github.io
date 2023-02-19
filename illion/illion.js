/* Conway's illion converter
https://kyodaisuu.github.io/illion/conway.html
Author: Fish
License: MIT License
*/

// Precision
const PREC = 10 // Numbers of digits after the decimal point to show
const DELTA = 2 ** -50 // Allowable relative error for the Newton method

// i18n
const LANG = document.getElementById('lang').textContent
const MESSAGE = {
  en: {
    help: 'Please input a number in either of the 2 boxes above.',
    result: 'Result',
    result1: ' is called',
    result2: 'in the ',
    result3: ' scale name of the Conway\'s illion system.',
    result4: '^ is calculated from right to left',
    urlhypere: 'https://googology.fandom.com/wiki/Hyper-E_notation',
    tetration: 'Tetration',
    urltetration: 'https://en.wikipedia.org/wiki/Tetration',
    permalink: 'Permalink of this result',
    clear: 'Clear',
    urlhere: 'conway.html',
    short: 'short',
    long: 'long',
    defaultscale: 'short',
    one: 'one',
    ten: 'ten',
    hundred: 'hundred',
    thousand: 'thousand',
    tre: 'tre',
    se: 'se',
    septe: 'septe',
    nove: 'nove',
    deci: 'deci'
  },
  fr: {
    help: 'Veuillez saisir un numéro dans l\'une des deux cases ci-dessus.',
    result: 'Résultat',
    result1: 'est appelé',
    result2: 'dans le nom de l\'échelle ',
    result3: ' du système des illion de Conway.',
    result4: '^ est calculé de droite à gauche',
    urlhypere: 'https://googology.fandom.com/fr/wiki/Notation_hyper-E',
    tetration: 'Tétration',
    urltetration: 'https://fr.wikipedia.org/wiki/T%C3%A9tration',
    permalink: 'Lien permanent de ce résultat',
    clear: 'Effacer',
    urlhere: 'conway-fr.html',
    short: 'échelle',
    long: 'longue',
    defaultscale: 'long',
    one: 'un',
    ten: 'dix',
    hundred: 'cent',
    thousand: 'mille',
    tre: 'tré',
    se: 'sé',
    septe: 'septé',
    nove: 'nové',
    deci: 'déci'
  }
}[LANG]

// Definition of Conway's system
const ISOLATE = ['ni', 'mi', 'bi', 'tri', 'quadri', 'quinti', 'sexti', 'septi', 'octi', 'noni']
const CW_UNI = ['', 'un', 'duo', MESSAGE.tre, 'quattuor', 'quin', MESSAGE.se, MESSAGE.septe, 'octo', MESSAGE.nove] // quinqua is changed to quin
const TEN = ['', MESSAGE.deci, 'viginti', 'triginta', 'quadraginta', 'quinquaginta', 'sexaginta', 'septuaginta', 'octoginta', 'nonaginta']
const HUN = ['', 'centi', 'ducenti', 'trecenti', 'quadringenti', 'quingenti', 'sescenti', 'septingenti', 'octingenti', 'nongenti']
const PREC_TEN = ['', 'N', 'MS', 'NS', 'NS', 'NS', 'N', 'N', 'MX', '']
const PREC_HUN = ['', 'NX', 'N', 'NS', 'NS', 'NS', 'N', 'N', 'MX', '']

window.onload = function () {
  initialize()
}

function updateIllion() {
  const textIllion = document.getElementById('illion').value
  if (!isNumeric(textIllion) || textIllion.includes('.') || Number(textIllion) < 1) {
    document.getElementById('power').value = ''
    clearResult()
    return
  }
  const illion = BigInt(textIllion)
  const scale = getScale()
  let p = illion * 3n + 3n
  if (scale === 'long') {
    p = illion * 6n
  }
  document.getElementById('factor').textContent = MESSAGE.one
  document.getElementById('power').value = p
  document.getElementById('suffix').textContent = 'on'
  showResult()
}

function updatePower() {
  const textPower = document.getElementById('power').value
  if (!isNumeric(textPower) || textPower.includes('.') || Number(textPower) < 1) {
    document.getElementById('illion').value = ''
    document.getElementById('suffix').textContent = 'on'
    clearResult()
    return
  }
  const power = BigInt(textPower)
  const scale = getScale()
  const factor = power % 3n
  const strFactor = [MESSAGE.one, MESSAGE.ten, MESSAGE.hundred][factor]
  if (power < 6n) {
    let name = strFactor
    if (power > 2n) {
      name += ` ${MESSAGE.thousand}`
    }
    document.getElementById('illion').value = ''
    document.getElementById('factor').textContent = MESSAGE.one
    let html = `<h2>${MESSAGE.result}</h2><p>${10 ** Number(power)} = <strong>${name}</strong></p>`
    html += `<p><a href="?power=${textPower}">${MESSAGE.permalink}</a> / <a href="${MESSAGE.urlhere}">${MESSAGE.clear}</a></p>`
    document.getElementById('result').innerHTML = html
    return
  }
  document.getElementById('factor').textContent = strFactor
  document.getElementById('suffix').textContent = 'on'
  let illion = (power - 3n) / 3n
  if (scale === 'long') {
    illion = power / 6n
    if (power / 3n % 2n === 1n) {
      document.getElementById('suffix').textContent = 'ard'
    }
  }
  document.getElementById('illion').value = illion
  showResult()
}

function showResult() {
  let html = `<h2>${MESSAGE.result}</h2>`
  html += `<ul><li>${calcIllion()}</li>`
  html += `<li>${calcDigit()}</li></ul>`
  html += permaLink()
  document.getElementById('result').innerHTML = html
}

function permaLink() {
  let textPower = document.getElementById('power').value
  textPower = textPower.trim().replace(/^0+/u, '')
  let permalink = `?power=${textPower}`
  if (getScale() !== MESSAGE.defaultscale) {
    permalink += `&scale=${getScale()}`
  }
  let html = `<p><a href="${permalink}">${MESSAGE.permalink}</a> / `
  html += `<a href="${MESSAGE.urlhere}">${MESSAGE.clear}</a></p>`
  return html
}

function initialize() {
  const scale = getParam('scale')
  if (scale === 'short') {
    document.getElementById('short').checked = true
  }
  if (scale === 'long') {
    document.getElementById('long').checked = true
  }
  let power = getParam('power')
  if (!isNumeric(power) || power.includes('.') || Number(power) < 1) {
    clearResult()
    document.getElementById('power').focus()
    return
  }
  power = power.trim().replace(/^0+/u, '')
  document.getElementById('power').value = power
  updatePower()
}

function getParam(name) {
  const url = location.href
  const regexS = `[\\?&]${name}=([^&#]*)`
  const regex = new RegExp(regexS)
  const results = regex.exec(url)
  if (results === null) {
    return null
  }
  return results[1]
}

function getScale() {
  const elements = document.getElementsByName('scale')
  let checkValue = ''
  for (let i = 0; i < elements.length; i++) {
    if (elements.item(i).checked) {
      checkValue = elements.item(i).value
    }
  }
  return checkValue
}

function isNumeric(str) {
  if (typeof str !== 'string') {
    return false
  }
  return !isNaN(str) && !isNaN(parseFloat(str))
}

function calcDigit() {
  const textIllion = document.getElementById('illion').value
  let textPower = document.getElementById('power').value
  textPower = textPower.trim().replace(/^0+/u, '')
  const power = BigInt(textPower)
  let output = `10<sup>${power}</sup>`
  if (power < 1000 && textIllion.length < 9) {
    output += ` = 1${'0'.repeat(Number(power))}`
  }
  if (power < 100 && textIllion.length < 9) {
    return output
  }
  const i = Number(`0.${textPower}`)
  let tower = textPower.length
  let science = ` &times; 10^${(tower - 1).toString()})`
  if (tower < PREC) {
    science = `<br>= 10^(${Number(textPower / 10 ** (tower - 1))}${science}`
  } else {
    science = `<br>&approx; 10^(${(i * 10).toFixed(PREC)}${science}`
  }
  tower += Math.log10(i)
  output += `${science}<br>&approx; 10^10^${tower.toFixed(PREC)} (${MESSAGE.result4})<br>`
  output += `= E${tower.toFixed(PREC)}#2 (<a href="${MESSAGE.urlhypere}">Hyper-E</a>)`
  let pt = 2
  const t = tower
  while (tower > 1) {
    tower = Math.log10(tower)
    pt += 1
    output += `<br>&approx; ${'10^'.repeat(pt)}${tower.toFixed(PREC)}`
    if (tower > 1) {
      output += `<br>= E${tower.toFixed(PREC)}#${pt}`
    }
  }
  output += `<br>= 10&uparrow;&uparrow;${(tower + pt - 1).toFixed(PREC)} `
  output += `(<a href="${MESSAGE.urltetration}">${MESSAGE.tetration}</a>)`
  output += `<br>&approx; 3&uparrow;&uparrow;${tet(t, 3).toFixed(PREC)}`
  output += `<br>&approx; e&uparrow;&uparrow;${tet(t, Math.E).toFixed(PREC)}`
  output += `<br>&approx; 2&uparrow;&uparrow;${tet(t, 2).toFixed(PREC)}`
  const st = stein(t)
  if (st < 4) {
    output += `<br>&approx; triangle(${(10 ** st).toFixed(PREC)})`
  } else {
    output += `<br>&approx; triangle(triangle(${stein2(st).toFixed(PREC)}))`
  }
  output += ' (<a href="https://en.wikipedia.org/wiki/Steinhaus%E2%80%93Moser_notation">Steinhaus</a>)'
  return output
}

function tet(n, b) {
  // Return x where 10^10^n = b^^x
  let tower = (n - Math.log10(Math.log10(b))) / Math.log10(b)
  let pt = 2
  while (tower > 1) {
    tower = Math.log2(tower) / Math.log2(b)
    pt += 1
  }
  return tower + pt - 1
}

function stein(n) {
  // Return x where 10^10^n = (10^x)^(10^x)
  // Solve f(x) = x + log10(x) - n = 0 with the Newton method
  let x = n - Math.log10(n)
  let p = 0
  while (Math.abs(x - p) > DELTA * p) {
    p = x
    const f = x + Math.log10(x) - n // f(x)
    const fp = 1 + 1 / x // f'(x)
    x -= f / fp
  }
  return x
}

function stein2(n) {
  // Return x where 10^n = x^x
  // Solve f(x) = x * log10(x) - n = 0 with the Newton method
  let x = n
  let p = 0
  const l10 = 1 / Math.log(10)
  while (Math.abs(x - p) > DELTA * p) {
    p = x
    const lx = Math.log10(x)
    const f = x * lx - n // f(x)
    const fp = l10 + lx // f'(x)
    x -= f / fp
  }
  return x
}

function calcIllion() {
  const textIllion = document.getElementById('illion').value
  const illion = BigInt(textIllion)
  const factor = document.getElementById('factor').textContent
  const suffix = document.getElementById('suffix').textContent
  if (isNaN(Number(illion)) || illion < 1) {
    return ''
  }
  const name = `${factor} ${llion(textIllion)}${suffix}`
  let textPower = document.getElementById('power').value
  textPower = textPower.trim().replace(/^0+/u, '')
  let output = `<p>10<sup>${textPower}</sup> ${MESSAGE.result1}<br>`
  output += `<strong>${name}</strong><br>`
  output += `${MESSAGE.result2}${MESSAGE[getScale()]}${MESSAGE.result3}</p>`
  return output
}

function clearResult() {
  document.getElementById('result').innerHTML = `<p>${MESSAGE.help}</p>`
}

function llion(n) {
  // Name of n-th illion number without the last 'on'
  n = n.trim()
  let intN = parseInt(n, 10)
  if (isNaN(intN) || intN < 1) {
    return ''
  }
  let name = ''
  while (n.length > 3) {
    name = base(parseInt(n.slice(-3), 10)) + name
    n = n.slice(0, -3)
  }
  intN = parseInt(n, 10)
  name = base(intN) + name
  return name
}

function base(n) {
  const unit = n % 10
  const ten = Math.floor(n / 10) % 10
  const hun = Math.floor(n / 100)
  if (n < 10) {
    return `${ISOLATE[n]}lli`
  }
  let prec = ''
  if (ten === 0) {
    prec = PREC_HUN[hun]
  } else {
    prec = PREC_TEN[ten]
  }
  let name = CW_UNI[unit]
  if (unit === 3 || unit === 6) {
    if (prec.includes('S')) {
      name = name.replace('é', 'e')
      name += 's'
    }
    if (prec.includes('X')) {
      if (unit === 3) {
        name = 'tres'
      } else {
        name = 'sex'
      }
    }
  }
  if (unit === 7 || unit === 9) {
    if (prec.includes('M')) {
      name = name.replace('é', 'e')
      name += 'm'
    }
    if (prec.includes('N')) {
      name = name.replace('é', 'e')
      name += 'n'
    }
  }
  name += TEN[ten]
  name += HUN[hun]
  name = `${name.slice(0, -1)}illi` // Replace the final vowel
  return name
}
