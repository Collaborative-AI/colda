/*! jQuery v3.5.1 | (c) JS Foundation and other contributors | jquery.org/license */
!(function (e, t) {
  'use strict'
  typeof module === 'object' && typeof module.exports === 'object'
    ? (module.exports = e.document
        ? t(e, !0)
        : function (e) {
            if (!e.document)
              throw new Error('jQuery requires a window with a document')
            return t(e)
          })
    : t(e)
})(typeof window !== 'undefined' ? window : this, function (C, e) {
  'use strict'
  const t = []
  const r = Object.getPrototypeOf
  const s = t.slice
  const g = t.flat
    ? function (e) {
        return t.flat.call(e)
      }
    : function (e) {
        return t.concat.apply([], e)
      }
  const u = t.push
  const i = t.indexOf
  const n = {}
  const o = n.toString
  const v = n.hasOwnProperty
  const a = v.toString
  const l = a.call(Object)
  const y = {}
  const m = function (e) {
    return typeof e === 'function' && typeof e.nodeType !== 'number'
  }
  const x = function (e) {
    return e != null && e === e.window
  }
  const E = C.document
  const c = { type: !0, src: !0, nonce: !0, noModule: !0 }
  function b(e, t, n) {
    let r
    let i
    const o = (n = n || E).createElement('script')
    if (((o.text = e), t))
      for (r in c)
        (i = t[r] || (t.getAttribute && t.getAttribute(r))) &&
          o.setAttribute(r, i)
    n.head.appendChild(o).parentNode.removeChild(o)
  }
  function w(e) {
    return e == null
      ? e + ''
      : typeof e === 'object' || typeof e === 'function'
      ? n[o.call(e)] || 'object'
      : typeof e
  }
  const f = '3.5.1'
  var S = function (e, t) {
    return new S.fn.init(e, t)
  }
  function p(e) {
    const t = !!e && 'length' in e && e.length
    const n = w(e)
    return (
      !m(e) &&
      !x(e) &&
      (n === 'array' ||
        t === 0 ||
        (typeof t === 'number' && t > 0 && t - 1 in e))
    )
  }
  ;(S.fn = S.prototype =
    {
      jquery: f,
      constructor: S,
      length: 0,
      toArray() {
        return s.call(this)
      },
      get(e) {
        return e == null
          ? s.call(this)
          : e < 0
          ? this[e + this.length]
          : this[e]
      },
      pushStack(e) {
        const t = S.merge(this.constructor(), e)
        return (t.prevObject = this), t
      },
      each(e) {
        return S.each(this, e)
      },
      map(n) {
        return this.pushStack(
          S.map(this, function (e, t) {
            return n.call(e, t, e)
          })
        )
      },
      slice() {
        return this.pushStack(s.apply(this, arguments))
      },
      first() {
        return this.eq(0)
      },
      last() {
        return this.eq(-1)
      },
      even() {
        return this.pushStack(
          S.grep(this, function (e, t) {
            return (t + 1) % 2
          })
        )
      },
      odd() {
        return this.pushStack(
          S.grep(this, function (e, t) {
            return t % 2
          })
        )
      },
      eq(e) {
        const t = this.length
        const n = +e + (e < 0 ? t : 0)
        return this.pushStack(n >= 0 && n < t ? [this[n]] : [])
      },
      end() {
        return this.prevObject || this.constructor()
      },
      push: u,
      sort: t.sort,
      splice: t.splice,
    }),
    (S.extend = S.fn.extend =
      function () {
        let e
        let t
        let n
        let r
        let i
        let o
        let a = arguments[0] || {}
        let s = 1
        const u = arguments.length
        let l = !1
        for (
          typeof a === 'boolean' && ((l = a), (a = arguments[s] || {}), s++),
            typeof a === 'object' || m(a) || (a = {}),
            s === u && ((a = this), s--);
          s < u;
          s++
        )
          if ((e = arguments[s]) != null)
            for (t in e)
              (r = e[t]),
                t !== '__proto__' &&
                  a !== r &&
                  (l && r && (S.isPlainObject(r) || (i = Array.isArray(r)))
                    ? ((n = a[t]),
                      (o =
                        i && !Array.isArray(n)
                          ? []
                          : i || S.isPlainObject(n)
                          ? n
                          : {}),
                      (i = !1),
                      (a[t] = S.extend(l, o, r)))
                    : void 0 !== r && (a[t] = r))
        return a
      }),
    S.extend({
      expando: 'jQuery' + (f + Math.random()).replace(/\D/g, ''),
      isReady: !0,
      error(e) {
        throw new Error(e)
      },
      noop() {},
      isPlainObject(e) {
        let t, n
        return (
          !(!e || o.call(e) !== '[object Object]') &&
          (!(t = r(e)) ||
            (typeof (n = v.call(t, 'constructor') && t.constructor) ===
              'function' &&
              a.call(n) === l))
        )
      },
      isEmptyObject(e) {
        let t
        for (t in e) return !1
        return !0
      },
      globalEval(e, t, n) {
        b(e, { nonce: t && t.nonce }, n)
      },
      each(e, t) {
        let n
        let r = 0
        if (p(e)) {
          for (n = e.length; r < n; r++) if (!1 === t.call(e[r], r, e[r])) break
        } else for (r in e) if (!1 === t.call(e[r], r, e[r])) break
        return e
      },
      makeArray(e, t) {
        const n = t || []
        return (
          e != null &&
            (p(Object(e))
              ? S.merge(n, typeof e === 'string' ? [e] : e)
              : u.call(n, e)),
          n
        )
      },
      inArray(e, t, n) {
        return t == null ? -1 : i.call(t, e, n)
      },
      merge(e, t) {
        for (var n = +t.length, r = 0, i = e.length; r < n; r++) e[i++] = t[r]
        return (e.length = i), e
      },
      grep(e, t, n) {
        for (var r = [], i = 0, o = e.length, a = !n; i < o; i++)
          !t(e[i], i) !== a && r.push(e[i])
        return r
      },
      map(e, t, n) {
        let r
        let i
        let o = 0
        const a = []
        if (p(e))
          for (r = e.length; o < r; o++)
            (i = t(e[o], o, n)) != null && a.push(i)
        else for (o in e) (i = t(e[o], o, n)) != null && a.push(i)
        return g(a)
      },
      guid: 1,
      support: y,
    }),
    typeof Symbol === 'function' &&
      (S.fn[Symbol.iterator] = t[Symbol.iterator]),
    S.each(
      'Boolean Number String Function Array Date RegExp Object Error Symbol'.split(
        ' '
      ),
      function (e, t) {
        n['[object ' + t + ']'] = t.toLowerCase()
      }
    )
  const d = (function (n) {
    let e
    let d
    let b
    let o
    let i
    let h
    let f
    let g
    let w
    let u
    let l
    let T
    let C
    let a
    let E
    let v
    let s
    let c
    let y
    const S = 'sizzle' + 1 * new Date()
    const p = n.document
    let k = 0
    let r = 0
    const m = ue()
    const x = ue()
    const A = ue()
    const N = ue()
    let D = function (e, t) {
      return e === t && (l = !0), 0
    }
    const j = {}.hasOwnProperty
    let t = []
    const q = t.pop
    const L = t.push
    let H = t.push
    const O = t.slice
    const P = function (e, t) {
      for (let n = 0, r = e.length; n < r; n++) if (e[n] === t) return n
      return -1
    }
    const R =
      'checked|selected|async|autofocus|autoplay|controls|defer|disabled|hidden|ismap|loop|multiple|open|readonly|required|scoped'
    const M = '[\\x20\\t\\r\\n\\f]'
    const I =
      '(?:\\\\[\\da-fA-F]{1,6}' + M + '?|\\\\[^\\r\\n\\f]|[\\w-]|[^\0-\\x7f])+'
    const W =
      '\\[' +
      M +
      '*(' +
      I +
      ')(?:' +
      M +
      '*([*^$|!~]?=)' +
      M +
      '*(?:\'((?:\\\\.|[^\\\\\'])*)\'|"((?:\\\\.|[^\\\\"])*)"|(' +
      I +
      '))|)' +
      M +
      '*\\]'
    const F =
      ':(' +
      I +
      ')(?:\\(((\'((?:\\\\.|[^\\\\\'])*)\'|"((?:\\\\.|[^\\\\"])*)")|((?:\\\\.|[^\\\\()[\\]]|' +
      W +
      ')*)|.*)\\)|)'
    const B = new RegExp(M + '+', 'g')
    const $ = new RegExp(
      '^' + M + '+|((?:^|[^\\\\])(?:\\\\.)*)' + M + '+$',
      'g'
    )
    const _ = new RegExp('^' + M + '*,' + M + '*')
    const z = new RegExp('^' + M + '*([>+~]|' + M + ')' + M + '*')
    const U = new RegExp(M + '|>')
    const X = new RegExp(F)
    const V = new RegExp('^' + I + '$')
    const G = {
      ID: new RegExp('^#(' + I + ')'),
      CLASS: new RegExp('^\\.(' + I + ')'),
      TAG: new RegExp('^(' + I + '|[*])'),
      ATTR: new RegExp('^' + W),
      PSEUDO: new RegExp('^' + F),
      CHILD: new RegExp(
        '^:(only|first|last|nth|nth-last)-(child|of-type)(?:\\(' +
          M +
          '*(even|odd|(([+-]|)(\\d*)n|)' +
          M +
          '*(?:([+-]|)' +
          M +
          '*(\\d+)|))' +
          M +
          '*\\)|)',
        'i'
      ),
      bool: new RegExp('^(?:' + R + ')$', 'i'),
      needsContext: new RegExp(
        '^' +
          M +
          '*[>+~]|:(even|odd|eq|gt|lt|nth|first|last)(?:\\(' +
          M +
          '*((?:-\\d)?\\d*)' +
          M +
          '*\\)|)(?=[^-]|$)',
        'i'
      ),
    }
    const Y = /HTML$/i
    const Q = /^(?:input|select|textarea|button)$/i
    const J = /^h\d$/i
    const K = /^[^{]+\{\s*\[native \w/
    const Z = /^(?:#([\w-]+)|(\w+)|\.([\w-]+))$/
    const ee = /[+~]/
    const te = new RegExp(
      '\\\\[\\da-fA-F]{1,6}' + M + '?|\\\\([^\\r\\n\\f])',
      'g'
    )
    const ne = function (e, t) {
      const n = '0x' + e.slice(1) - 65536
      return (
        t ||
        (n < 0
          ? String.fromCharCode(n + 65536)
          : String.fromCharCode((n >> 10) | 55296, (1023 & n) | 56320))
      )
    }
    const re = /([\0-\x1F\x7F]|^-?\d)|^-$|[^\0-\x1F\x7F-\uFFFF\w-]/g
    const ie = function (e, t) {
      return t
        ? e === '\0'
          ? '\uFFFD'
          : e.slice(0, -1) +
            '\\' +
            e.charCodeAt(e.length - 1).toString(16) +
            ' '
        : '\\' + e
    }
    const oe = function () {
      T()
    }
    const ae = be(
      function (e) {
        return !0 === e.disabled && e.nodeName.toLowerCase() === 'fieldset'
      },
      { dir: 'parentNode', next: 'legend' }
    )
    try {
      H.apply((t = O.call(p.childNodes)), p.childNodes),
        t[p.childNodes.length].nodeType
    } catch (e) {
      H = {
        apply: t.length
          ? function (e, t) {
              L.apply(e, O.call(t))
            }
          : function (e, t) {
              let n = e.length
              let r = 0
              while ((e[n++] = t[r++]));
              e.length = n - 1
            },
      }
    }
    function se(t, e, n, r) {
      let i
      let o
      let a
      let s
      let u
      let l
      let c
      let f = e && e.ownerDocument
      const p = e ? e.nodeType : 9
      if (
        ((n = n || []),
        typeof t !== 'string' || !t || (p !== 1 && p !== 9 && p !== 11))
      )
        return n
      if (!r && (T(e), (e = e || C), E)) {
        if (p !== 11 && (u = Z.exec(t)))
          if ((i = u[1])) {
            if (p === 9) {
              if (!(a = e.getElementById(i))) return n
              if (a.id === i) return n.push(a), n
            } else if (f && (a = f.getElementById(i)) && y(e, a) && a.id === i)
              return n.push(a), n
          } else {
            if (u[2]) return H.apply(n, e.getElementsByTagName(t)), n
            if (
              (i = u[3]) &&
              d.getElementsByClassName &&
              e.getElementsByClassName
            )
              return H.apply(n, e.getElementsByClassName(i)), n
          }
        if (
          d.qsa &&
          !N[t + ' '] &&
          (!v || !v.test(t)) &&
          (p !== 1 || e.nodeName.toLowerCase() !== 'object')
        ) {
          if (((c = t), (f = e), p === 1 && (U.test(t) || z.test(t)))) {
            ;((f = (ee.test(t) && ye(e.parentNode)) || e) === e && d.scope) ||
              ((s = e.getAttribute('id'))
                ? (s = s.replace(re, ie))
                : e.setAttribute('id', (s = S))),
              (o = (l = h(t)).length)
            while (o--) l[o] = (s ? '#' + s : ':scope') + ' ' + xe(l[o])
            c = l.join(',')
          }
          try {
            return H.apply(n, f.querySelectorAll(c)), n
          } catch (e) {
            N(t, !0)
          } finally {
            s === S && e.removeAttribute('id')
          }
        }
      }
      return g(t.replace($, '$1'), e, n, r)
    }
    function ue() {
      const r = []
      return function e(t, n) {
        return (
          r.push(t + ' ') > b.cacheLength && delete e[r.shift()],
          (e[t + ' '] = n)
        )
      }
    }
    function le(e) {
      return (e[S] = !0), e
    }
    function ce(e) {
      let t = C.createElement('fieldset')
      try {
        return !!e(t)
      } catch (e) {
        return !1
      } finally {
        t.parentNode && t.parentNode.removeChild(t), (t = null)
      }
    }
    function fe(e, t) {
      const n = e.split('|')
      let r = n.length
      while (r--) b.attrHandle[n[r]] = t
    }
    function pe(e, t) {
      let n = t && e
      const r =
        n &&
        e.nodeType === 1 &&
        t.nodeType === 1 &&
        e.sourceIndex - t.sourceIndex
      if (r) return r
      if (n) while ((n = n.nextSibling)) if (n === t) return -1
      return e ? 1 : -1
    }
    function de(t) {
      return function (e) {
        return e.nodeName.toLowerCase() === 'input' && e.type === t
      }
    }
    function he(n) {
      return function (e) {
        const t = e.nodeName.toLowerCase()
        return (t === 'input' || t === 'button') && e.type === n
      }
    }
    function ge(t) {
      return function (e) {
        return 'form' in e
          ? e.parentNode && !1 === e.disabled
            ? 'label' in e
              ? 'label' in e.parentNode
                ? e.parentNode.disabled === t
                : e.disabled === t
              : e.isDisabled === t || (e.isDisabled !== !t && ae(e) === t)
            : e.disabled === t
          : 'label' in e && e.disabled === t
      }
    }
    function ve(a) {
      return le(function (o) {
        return (
          (o = +o),
          le(function (e, t) {
            let n
            const r = a([], e.length, o)
            let i = r.length
            while (i--) e[(n = r[i])] && (e[n] = !(t[n] = e[n]))
          })
        )
      })
    }
    function ye(e) {
      return e && typeof e.getElementsByTagName !== 'undefined' && e
    }
    for (e in ((d = se.support = {}),
    (i = se.isXML =
      function (e) {
        const t = e.namespaceURI
        const n = (e.ownerDocument || e).documentElement
        return !Y.test(t || (n && n.nodeName) || 'HTML')
      }),
    (T = se.setDocument =
      function (e) {
        let t
        let n
        const r = e ? e.ownerDocument || e : p
        return (
          r != C &&
            r.nodeType === 9 &&
            r.documentElement &&
            ((a = (C = r).documentElement),
            (E = !i(C)),
            p != C &&
              (n = C.defaultView) &&
              n.top !== n &&
              (n.addEventListener
                ? n.addEventListener('unload', oe, !1)
                : n.attachEvent && n.attachEvent('onunload', oe)),
            (d.scope = ce(function (e) {
              return (
                a.appendChild(e).appendChild(C.createElement('div')),
                typeof e.querySelectorAll !== 'undefined' &&
                  !e.querySelectorAll(':scope fieldset div').length
              )
            })),
            (d.attributes = ce(function (e) {
              return (e.className = 'i'), !e.getAttribute('className')
            })),
            (d.getElementsByTagName = ce(function (e) {
              return (
                e.appendChild(C.createComment('')),
                !e.getElementsByTagName('*').length
              )
            })),
            (d.getElementsByClassName = K.test(C.getElementsByClassName)),
            (d.getById = ce(function (e) {
              return (
                (a.appendChild(e).id = S),
                !C.getElementsByName || !C.getElementsByName(S).length
              )
            })),
            d.getById
              ? ((b.filter.ID = function (e) {
                  const t = e.replace(te, ne)
                  return function (e) {
                    return e.getAttribute('id') === t
                  }
                }),
                (b.find.ID = function (e, t) {
                  if (typeof t.getElementById !== 'undefined' && E) {
                    const n = t.getElementById(e)
                    return n ? [n] : []
                  }
                }))
              : ((b.filter.ID = function (e) {
                  const n = e.replace(te, ne)
                  return function (e) {
                    const t =
                      typeof e.getAttributeNode !== 'undefined' &&
                      e.getAttributeNode('id')
                    return t && t.value === n
                  }
                }),
                (b.find.ID = function (e, t) {
                  if (typeof t.getElementById !== 'undefined' && E) {
                    let n
                    let r
                    let i
                    let o = t.getElementById(e)
                    if (o) {
                      if ((n = o.getAttributeNode('id')) && n.value === e)
                        return [o]
                      ;(i = t.getElementsByName(e)), (r = 0)
                      while ((o = i[r++]))
                        if ((n = o.getAttributeNode('id')) && n.value === e)
                          return [o]
                    }
                    return []
                  }
                })),
            (b.find.TAG = d.getElementsByTagName
              ? function (e, t) {
                  return typeof t.getElementsByTagName !== 'undefined'
                    ? t.getElementsByTagName(e)
                    : d.qsa
                    ? t.querySelectorAll(e)
                    : void 0
                }
              : function (e, t) {
                  let n
                  const r = []
                  let i = 0
                  const o = t.getElementsByTagName(e)
                  if (e === '*') {
                    while ((n = o[i++])) n.nodeType === 1 && r.push(n)
                    return r
                  }
                  return o
                }),
            (b.find.CLASS =
              d.getElementsByClassName &&
              function (e, t) {
                if (typeof t.getElementsByClassName !== 'undefined' && E)
                  return t.getElementsByClassName(e)
              }),
            (s = []),
            (v = []),
            (d.qsa = K.test(C.querySelectorAll)) &&
              (ce(function (e) {
                let t
                ;(a.appendChild(e).innerHTML =
                  "<a id='" +
                  S +
                  "'></a><select id='" +
                  S +
                  "-\r\\' msallowcapture=''><option selected=''></option></select>"),
                  e.querySelectorAll("[msallowcapture^='']").length &&
                    v.push('[*^$]=' + M + '*(?:\'\'|"")'),
                  e.querySelectorAll('[selected]').length ||
                    v.push('\\[' + M + '*(?:value|' + R + ')'),
                  e.querySelectorAll('[id~=' + S + '-]').length || v.push('~='),
                  (t = C.createElement('input')).setAttribute('name', ''),
                  e.appendChild(t),
                  e.querySelectorAll("[name='']").length ||
                    v.push('\\[' + M + '*name' + M + '*=' + M + '*(?:\'\'|"")'),
                  e.querySelectorAll(':checked').length || v.push(':checked'),
                  e.querySelectorAll('a#' + S + '+*').length ||
                    v.push('.#.+[+~]'),
                  e.querySelectorAll('\\\f'),
                  v.push('[\\r\\n\\f]')
              }),
              ce(function (e) {
                e.innerHTML =
                  "<a href='' disabled='disabled'></a><select disabled='disabled'><option/></select>"
                const t = C.createElement('input')
                t.setAttribute('type', 'hidden'),
                  e.appendChild(t).setAttribute('name', 'D'),
                  e.querySelectorAll('[name=d]').length &&
                    v.push('name' + M + '*[*^$|!~]?='),
                  e.querySelectorAll(':enabled').length !== 2 &&
                    v.push(':enabled', ':disabled'),
                  (a.appendChild(e).disabled = !0),
                  e.querySelectorAll(':disabled').length !== 2 &&
                    v.push(':enabled', ':disabled'),
                  e.querySelectorAll('*,:x'),
                  v.push(',.*:')
              })),
            (d.matchesSelector = K.test(
              (c =
                a.matches ||
                a.webkitMatchesSelector ||
                a.mozMatchesSelector ||
                a.oMatchesSelector ||
                a.msMatchesSelector)
            )) &&
              ce(function (e) {
                ;(d.disconnectedMatch = c.call(e, '*')),
                  c.call(e, "[s!='']:x"),
                  s.push('!=', F)
              }),
            (v = v.length && new RegExp(v.join('|'))),
            (s = s.length && new RegExp(s.join('|'))),
            (t = K.test(a.compareDocumentPosition)),
            (y =
              t || K.test(a.contains)
                ? function (e, t) {
                    const n = e.nodeType === 9 ? e.documentElement : e
                    const r = t && t.parentNode
                    return (
                      e === r ||
                      !(
                        !r ||
                        r.nodeType !== 1 ||
                        !(n.contains
                          ? n.contains(r)
                          : e.compareDocumentPosition &&
                            16 & e.compareDocumentPosition(r))
                      )
                    )
                  }
                : function (e, t) {
                    if (t) while ((t = t.parentNode)) if (t === e) return !0
                    return !1
                  }),
            (D = t
              ? function (e, t) {
                  if (e === t) return (l = !0), 0
                  let n =
                    !e.compareDocumentPosition - !t.compareDocumentPosition
                  return (
                    n ||
                    (1 &
                      (n =
                        (e.ownerDocument || e) == (t.ownerDocument || t)
                          ? e.compareDocumentPosition(t)
                          : 1) ||
                    (!d.sortDetached && t.compareDocumentPosition(e) === n)
                      ? e == C || (e.ownerDocument == p && y(p, e))
                        ? -1
                        : t == C || (t.ownerDocument == p && y(p, t))
                        ? 1
                        : u
                        ? P(u, e) - P(u, t)
                        : 0
                      : 4 & n
                      ? -1
                      : 1)
                  )
                }
              : function (e, t) {
                  if (e === t) return (l = !0), 0
                  let n
                  let r = 0
                  const i = e.parentNode
                  const o = t.parentNode
                  const a = [e]
                  const s = [t]
                  if (!i || !o)
                    return e == C
                      ? -1
                      : t == C
                      ? 1
                      : i
                      ? -1
                      : o
                      ? 1
                      : u
                      ? P(u, e) - P(u, t)
                      : 0
                  if (i === o) return pe(e, t)
                  n = e
                  while ((n = n.parentNode)) a.unshift(n)
                  n = t
                  while ((n = n.parentNode)) s.unshift(n)
                  while (a[r] === s[r]) r++
                  return r ? pe(a[r], s[r]) : a[r] == p ? -1 : s[r] == p ? 1 : 0
                })),
          C
        )
      }),
    (se.matches = function (e, t) {
      return se(e, null, null, t)
    }),
    (se.matchesSelector = function (e, t) {
      if (
        (T(e),
        d.matchesSelector &&
          E &&
          !N[t + ' '] &&
          (!s || !s.test(t)) &&
          (!v || !v.test(t)))
      )
        try {
          const n = c.call(e, t)
          if (
            n ||
            d.disconnectedMatch ||
            (e.document && e.document.nodeType !== 11)
          )
            return n
        } catch (e) {
          N(t, !0)
        }
      return se(t, C, null, [e]).length > 0
    }),
    (se.contains = function (e, t) {
      return (e.ownerDocument || e) != C && T(e), y(e, t)
    }),
    (se.attr = function (e, t) {
      ;(e.ownerDocument || e) != C && T(e)
      const n = b.attrHandle[t.toLowerCase()]
      let r = n && j.call(b.attrHandle, t.toLowerCase()) ? n(e, t, !E) : void 0
      return void 0 !== r
        ? r
        : d.attributes || !E
        ? e.getAttribute(t)
        : (r = e.getAttributeNode(t)) && r.specified
        ? r.value
        : null
    }),
    (se.escape = function (e) {
      return (e + '').replace(re, ie)
    }),
    (se.error = function (e) {
      throw new Error('Syntax error, unrecognized expression: ' + e)
    }),
    (se.uniqueSort = function (e) {
      let t
      const n = []
      let r = 0
      let i = 0
      if (
        ((l = !d.detectDuplicates),
        (u = !d.sortStable && e.slice(0)),
        e.sort(D),
        l)
      ) {
        while ((t = e[i++])) t === e[i] && (r = n.push(i))
        while (r--) e.splice(n[r], 1)
      }
      return (u = null), e
    }),
    (o = se.getText =
      function (e) {
        let t
        let n = ''
        let r = 0
        const i = e.nodeType
        if (i) {
          if (i === 1 || i === 9 || i === 11) {
            if (typeof e.textContent === 'string') return e.textContent
            for (e = e.firstChild; e; e = e.nextSibling) n += o(e)
          } else if (i === 3 || i === 4) return e.nodeValue
        } else while ((t = e[r++])) n += o(t)
        return n
      }),
    ((b = se.selectors =
      {
        cacheLength: 50,
        createPseudo: le,
        match: G,
        attrHandle: {},
        find: {},
        relative: {
          '>': { dir: 'parentNode', first: !0 },
          ' ': { dir: 'parentNode' },
          '+': { dir: 'previousSibling', first: !0 },
          '~': { dir: 'previousSibling' },
        },
        preFilter: {
          ATTR(e) {
            return (
              (e[1] = e[1].replace(te, ne)),
              (e[3] = (e[3] || e[4] || e[5] || '').replace(te, ne)),
              e[2] === '~=' && (e[3] = ' ' + e[3] + ' '),
              e.slice(0, 4)
            )
          },
          CHILD(e) {
            return (
              (e[1] = e[1].toLowerCase()),
              e[1].slice(0, 3) === 'nth'
                ? (e[3] || se.error(e[0]),
                  (e[4] = +(e[4]
                    ? e[5] + (e[6] || 1)
                    : 2 * (e[3] === 'even' || e[3] === 'odd'))),
                  (e[5] = +(e[7] + e[8] || e[3] === 'odd')))
                : e[3] && se.error(e[0]),
              e
            )
          },
          PSEUDO(e) {
            let t
            const n = !e[6] && e[2]
            return G.CHILD.test(e[0])
              ? null
              : (e[3]
                  ? (e[2] = e[4] || e[5] || '')
                  : n &&
                    X.test(n) &&
                    (t = h(n, !0)) &&
                    (t = n.indexOf(')', n.length - t) - n.length) &&
                    ((e[0] = e[0].slice(0, t)), (e[2] = n.slice(0, t))),
                e.slice(0, 3))
          },
        },
        filter: {
          TAG(e) {
            const t = e.replace(te, ne).toLowerCase()
            return e === '*'
              ? function () {
                  return !0
                }
              : function (e) {
                  return e.nodeName && e.nodeName.toLowerCase() === t
                }
          },
          CLASS(e) {
            let t = m[e + ' ']
            return (
              t ||
              ((t = new RegExp('(^|' + M + ')' + e + '(' + M + '|$)')) &&
                m(e, function (e) {
                  return t.test(
                    (typeof e.className === 'string' && e.className) ||
                      (typeof e.getAttribute !== 'undefined' &&
                        e.getAttribute('class')) ||
                      ''
                  )
                }))
            )
          },
          ATTR(n, r, i) {
            return function (e) {
              let t = se.attr(e, n)
              return t == null
                ? r === '!='
                : !r ||
                    ((t += ''),
                    r === '='
                      ? t === i
                      : r === '!='
                      ? t !== i
                      : r === '^='
                      ? i && t.indexOf(i) === 0
                      : r === '*='
                      ? i && t.includes(i)
                      : r === '$='
                      ? i && t.slice(-i.length) === i
                      : r === '~='
                      ? (' ' + t.replace(B, ' ') + ' ').includes(i)
                      : r === '|=' &&
                        (t === i || t.slice(0, i.length + 1) === i + '-'))
            }
          },
          CHILD(h, e, t, g, v) {
            const y = h.slice(0, 3) !== 'nth'
            const m = h.slice(-4) !== 'last'
            const x = e === 'of-type'
            return g === 1 && v === 0
              ? function (e) {
                  return !!e.parentNode
                }
              : function (e, t, n) {
                  let r
                  let i
                  let o
                  let a
                  let s
                  let u
                  let l = y !== m ? 'nextSibling' : 'previousSibling'
                  const c = e.parentNode
                  const f = x && e.nodeName.toLowerCase()
                  const p = !n && !x
                  let d = !1
                  if (c) {
                    if (y) {
                      while (l) {
                        a = e
                        while ((a = a[l]))
                          if (
                            x
                              ? a.nodeName.toLowerCase() === f
                              : a.nodeType === 1
                          )
                            return !1
                        u = l = h === 'only' && !u && 'nextSibling'
                      }
                      return !0
                    }
                    if (((u = [m ? c.firstChild : c.lastChild]), m && p)) {
                      ;(d =
                        (s =
                          (r =
                            (i =
                              (o = (a = c)[S] || (a[S] = {}))[a.uniqueID] ||
                              (o[a.uniqueID] = {}))[h] || [])[0] === k &&
                          r[1]) && r[2]),
                        (a = s && c.childNodes[s])
                      while ((a = (++s && a && a[l]) || (d = s = 0) || u.pop()))
                        if (a.nodeType === 1 && ++d && a === e) {
                          i[h] = [k, s, d]
                          break
                        }
                    } else if (
                      (p &&
                        (d = s =
                          (r =
                            (i =
                              (o = (a = e)[S] || (a[S] = {}))[a.uniqueID] ||
                              (o[a.uniqueID] = {}))[h] || [])[0] === k && r[1]),
                      !1 === d)
                    )
                      while ((a = (++s && a && a[l]) || (d = s = 0) || u.pop()))
                        if (
                          (x
                            ? a.nodeName.toLowerCase() === f
                            : a.nodeType === 1) &&
                          ++d &&
                          (p &&
                            ((i =
                              (o = a[S] || (a[S] = {}))[a.uniqueID] ||
                              (o[a.uniqueID] = {}))[h] = [k, d]),
                          a === e)
                        )
                          break
                    return (d -= v) === g || (d % g == 0 && d / g >= 0)
                  }
                }
          },
          PSEUDO(e, o) {
            let t
            const a =
              b.pseudos[e] ||
              b.setFilters[e.toLowerCase()] ||
              se.error('unsupported pseudo: ' + e)
            return a[S]
              ? a(o)
              : a.length > 1
              ? ((t = [e, e, '', o]),
                b.setFilters.hasOwnProperty(e.toLowerCase())
                  ? le(function (e, t) {
                      let n
                      const r = a(e, o)
                      let i = r.length
                      while (i--) e[(n = P(e, r[i]))] = !(t[n] = r[i])
                    })
                  : function (e) {
                      return a(e, 0, t)
                    })
              : a
          },
        },
        pseudos: {
          not: le(function (e) {
            const r = []
            const i = []
            const s = f(e.replace($, '$1'))
            return s[S]
              ? le(function (e, t, n, r) {
                  let i
                  const o = s(e, null, r, [])
                  let a = e.length
                  while (a--) (i = o[a]) && (e[a] = !(t[a] = i))
                })
              : function (e, t, n) {
                  return (r[0] = e), s(r, null, n, i), (r[0] = null), !i.pop()
                }
          }),
          has: le(function (t) {
            return function (e) {
              return se(t, e).length > 0
            }
          }),
          contains: le(function (t) {
            return (
              (t = t.replace(te, ne)),
              function (e) {
                return (e.textContent || o(e)).includes(t)
              }
            )
          }),
          lang: le(function (n) {
            return (
              V.test(n || '') || se.error('unsupported lang: ' + n),
              (n = n.replace(te, ne).toLowerCase()),
              function (e) {
                let t
                do {
                  if (
                    (t = E
                      ? e.lang
                      : e.getAttribute('xml:lang') || e.getAttribute('lang'))
                  )
                    return (
                      (t = t.toLowerCase()) === n || t.indexOf(n + '-') === 0
                    )
                } while ((e = e.parentNode) && e.nodeType === 1)
                return !1
              }
            )
          }),
          target(e) {
            const t = n.location && n.location.hash
            return t && t.slice(1) === e.id
          },
          root(e) {
            return e === a
          },
          focus(e) {
            return (
              e === C.activeElement &&
              (!C.hasFocus || C.hasFocus()) &&
              !!(e.type || e.href || ~e.tabIndex)
            )
          },
          enabled: ge(!1),
          disabled: ge(!0),
          checked(e) {
            const t = e.nodeName.toLowerCase()
            return (
              (t === 'input' && !!e.checked) || (t === 'option' && !!e.selected)
            )
          },
          selected(e) {
            return e.parentNode && e.parentNode.selectedIndex, !0 === e.selected
          },
          empty(e) {
            for (e = e.firstChild; e; e = e.nextSibling)
              if (e.nodeType < 6) return !1
            return !0
          },
          parent(e) {
            return !b.pseudos.empty(e)
          },
          header(e) {
            return J.test(e.nodeName)
          },
          input(e) {
            return Q.test(e.nodeName)
          },
          button(e) {
            const t = e.nodeName.toLowerCase()
            return (t === 'input' && e.type === 'button') || t === 'button'
          },
          text(e) {
            let t
            return (
              e.nodeName.toLowerCase() === 'input' &&
              e.type === 'text' &&
              ((t = e.getAttribute('type')) == null ||
                t.toLowerCase() === 'text')
            )
          },
          first: ve(function () {
            return [0]
          }),
          last: ve(function (e, t) {
            return [t - 1]
          }),
          eq: ve(function (e, t, n) {
            return [n < 0 ? n + t : n]
          }),
          even: ve(function (e, t) {
            for (let n = 0; n < t; n += 2) e.push(n)
            return e
          }),
          odd: ve(function (e, t) {
            for (let n = 1; n < t; n += 2) e.push(n)
            return e
          }),
          lt: ve(function (e, t, n) {
            for (let r = n < 0 ? n + t : t < n ? t : n; --r >= 0; ) e.push(r)
            return e
          }),
          gt: ve(function (e, t, n) {
            for (let r = n < 0 ? n + t : n; ++r < t; ) e.push(r)
            return e
          }),
        },
      }).pseudos.nth = b.pseudos.eq),
    { radio: !0, checkbox: !0, file: !0, password: !0, image: !0 }))
      b.pseudos[e] = de(e)
    for (e in { submit: !0, reset: !0 }) b.pseudos[e] = he(e)
    function me() {}
    function xe(e) {
      for (var t = 0, n = e.length, r = ''; t < n; t++) r += e[t].value
      return r
    }
    function be(s, e, t) {
      const u = e.dir
      const l = e.next
      const c = l || u
      const f = t && c === 'parentNode'
      const p = r++
      return e.first
        ? function (e, t, n) {
            while ((e = e[u])) if (e.nodeType === 1 || f) return s(e, t, n)
            return !1
          }
        : function (e, t, n) {
            let r
            let i
            let o
            const a = [k, p]
            if (n) {
              while ((e = e[u]))
                if ((e.nodeType === 1 || f) && s(e, t, n)) return !0
            } else
              while ((e = e[u]))
                if (e.nodeType === 1 || f)
                  if (
                    ((i =
                      (o = e[S] || (e[S] = {}))[e.uniqueID] ||
                      (o[e.uniqueID] = {})),
                    l && l === e.nodeName.toLowerCase())
                  )
                    e = e[u] || e
                  else {
                    if ((r = i[c]) && r[0] === k && r[1] === p)
                      return (a[2] = r[2])
                    if (((i[c] = a)[2] = s(e, t, n))) return !0
                  }
            return !1
          }
    }
    function we(i) {
      return i.length > 1
        ? function (e, t, n) {
            let r = i.length
            while (r--) if (!i[r](e, t, n)) return !1
            return !0
          }
        : i[0]
    }
    function Te(e, t, n, r, i) {
      for (var o, a = [], s = 0, u = e.length, l = t != null; s < u; s++)
        (o = e[s]) && ((n && !n(o, r, i)) || (a.push(o), l && t.push(s)))
      return a
    }
    function Ce(d, h, g, v, y, e) {
      return (
        v && !v[S] && (v = Ce(v)),
        y && !y[S] && (y = Ce(y, e)),
        le(function (e, t, n, r) {
          let i
          let o
          let a
          const s = []
          const u = []
          const l = t.length
          const c =
            e ||
            (function (e, t, n) {
              for (let r = 0, i = t.length; r < i; r++) se(e, t[r], n)
              return n
            })(h || '*', n.nodeType ? [n] : n, [])
          const f = !d || (!e && h) ? c : Te(c, s, d, n, r)
          let p = g ? (y || (e ? d : l || v) ? [] : t) : f
          if ((g && g(f, p, n, r), v)) {
            ;(i = Te(p, u)), v(i, [], n, r), (o = i.length)
            while (o--) (a = i[o]) && (p[u[o]] = !(f[u[o]] = a))
          }
          if (e) {
            if (y || d) {
              if (y) {
                ;(i = []), (o = p.length)
                while (o--) (a = p[o]) && i.push((f[o] = a))
                y(null, (p = []), i, r)
              }
              o = p.length
              while (o--)
                (a = p[o]) &&
                  (i = y ? P(e, a) : s[o]) > -1 &&
                  (e[i] = !(t[i] = a))
            }
          } else (p = Te(p === t ? p.splice(l, p.length) : p)), y ? y(null, t, p, r) : H.apply(t, p)
        })
      )
    }
    function Ee(e) {
      for (
        var i,
          t,
          n,
          r = e.length,
          o = b.relative[e[0].type],
          a = o || b.relative[' '],
          s = o ? 1 : 0,
          u = be(
            function (e) {
              return e === i
            },
            a,
            !0
          ),
          l = be(
            function (e) {
              return P(i, e) > -1
            },
            a,
            !0
          ),
          c = [
            function (e, t, n) {
              const r =
                (!o && (n || t !== w)) ||
                ((i = t).nodeType ? u(e, t, n) : l(e, t, n))
              return (i = null), r
            },
          ];
        s < r;
        s++
      )
        if ((t = b.relative[e[s].type])) c = [be(we(c), t)]
        else {
          if ((t = b.filter[e[s].type].apply(null, e[s].matches))[S]) {
            for (n = ++s; n < r; n++) if (b.relative[e[n].type]) break
            return Ce(
              s > 1 && we(c),
              s > 1 &&
                xe(
                  e
                    .slice(0, s - 1)
                    .concat({ value: e[s - 2].type === ' ' ? '*' : '' })
                ).replace($, '$1'),
              t,
              s < n && Ee(e.slice(s, n)),
              n < r && Ee((e = e.slice(n))),
              n < r && xe(e)
            )
          }
          c.push(t)
        }
      return we(c)
    }
    return (
      (me.prototype = b.filters = b.pseudos),
      (b.setFilters = new me()),
      (h = se.tokenize =
        function (e, t) {
          let n
          let r
          let i
          let o
          let a
          let s
          let u
          const l = x[e + ' ']
          if (l) return t ? 0 : l.slice(0)
          ;(a = e), (s = []), (u = b.preFilter)
          while (a) {
            for (o in ((n && !(r = _.exec(a))) ||
              (r && (a = a.slice(r[0].length) || a), s.push((i = []))),
            (n = !1),
            (r = z.exec(a)) &&
              ((n = r.shift()),
              i.push({ value: n, type: r[0].replace($, ' ') }),
              (a = a.slice(n.length))),
            b.filter))
              !(r = G[o].exec(a)) ||
                (u[o] && !(r = u[o](r))) ||
                ((n = r.shift()),
                i.push({ value: n, type: o, matches: r }),
                (a = a.slice(n.length)))
            if (!n) break
          }
          return t ? a.length : a ? se.error(e) : x(e, s).slice(0)
        }),
      (f = se.compile =
        function (e, t) {
          let n
          let v
          let y
          let m
          let x
          let r
          const i = []
          const o = []
          let a = A[e + ' ']
          if (!a) {
            t || (t = h(e)), (n = t.length)
            while (n--) (a = Ee(t[n]))[S] ? i.push(a) : o.push(a)
            ;(a = A(
              e,
              ((v = o),
              (m = (y = i).length > 0),
              (x = v.length > 0),
              (r = function (e, t, n, r, i) {
                let o
                let a
                let s
                let u = 0
                let l = '0'
                const c = e && []
                let f = []
                const p = w
                const d = e || (x && b.find.TAG('*', i))
                const h = (k += p == null ? 1 : Math.random() || 0.1)
                const g = d.length
                for (
                  i && (w = t == C || t || i);
                  l !== g && (o = d[l]) != null;
                  l++
                ) {
                  if (x && o) {
                    ;(a = 0), t || o.ownerDocument == C || (T(o), (n = !E))
                    while ((s = v[a++]))
                      if (s(o, t || C, n)) {
                        r.push(o)
                        break
                      }
                    i && (k = h)
                  }
                  m && ((o = !s && o) && u--, e && c.push(o))
                }
                if (((u += l), m && l !== u)) {
                  a = 0
                  while ((s = y[a++])) s(c, f, t, n)
                  if (e) {
                    if (u > 0) while (l--) c[l] || f[l] || (f[l] = q.call(r))
                    f = Te(f)
                  }
                  H.apply(r, f),
                    i &&
                      !e &&
                      f.length > 0 &&
                      u + y.length > 1 &&
                      se.uniqueSort(r)
                }
                return i && ((k = h), (w = p)), c
              }),
              m ? le(r) : r)
            )).selector = e
          }
          return a
        }),
      (g = se.select =
        function (e, t, n, r) {
          let i
          let o
          let a
          let s
          let u
          const l = typeof e === 'function' && e
          const c = !r && h((e = l.selector || e))
          if (((n = n || []), c.length === 1)) {
            if (
              (o = c[0] = c[0].slice(0)).length > 2 &&
              (a = o[0]).type === 'ID' &&
              t.nodeType === 9 &&
              E &&
              b.relative[o[1].type]
            ) {
              if (!(t = (b.find.ID(a.matches[0].replace(te, ne), t) || [])[0]))
                return n
              l && (t = t.parentNode), (e = e.slice(o.shift().value.length))
            }
            i = G.needsContext.test(e) ? 0 : o.length
            while (i--) {
              if (((a = o[i]), b.relative[(s = a.type)])) break
              if (
                (u = b.find[s]) &&
                (r = u(
                  a.matches[0].replace(te, ne),
                  (ee.test(o[0].type) && ye(t.parentNode)) || t
                ))
              ) {
                if ((o.splice(i, 1), !(e = r.length && xe(o))))
                  return H.apply(n, r), n
                break
              }
            }
          }
          return (
            (l || f(e, c))(
              r,
              t,
              !E,
              n,
              !t || (ee.test(e) && ye(t.parentNode)) || t
            ),
            n
          )
        }),
      (d.sortStable = S.split('').sort(D).join('') === S),
      (d.detectDuplicates = !!l),
      T(),
      (d.sortDetached = ce(function (e) {
        return 1 & e.compareDocumentPosition(C.createElement('fieldset'))
      })),
      ce(function (e) {
        return (
          (e.innerHTML = "<a href='#'></a>"),
          e.firstChild.getAttribute('href') === '#'
        )
      }) ||
        fe('type|href|height|width', function (e, t, n) {
          if (!n) return e.getAttribute(t, t.toLowerCase() === 'type' ? 1 : 2)
        }),
      (d.attributes &&
        ce(function (e) {
          return (
            (e.innerHTML = '<input/>'),
            e.firstChild.setAttribute('value', ''),
            e.firstChild.getAttribute('value') === ''
          )
        })) ||
        fe('value', function (e, t, n) {
          if (!n && e.nodeName.toLowerCase() === 'input') return e.defaultValue
        }),
      ce(function (e) {
        return e.getAttribute('disabled') == null
      }) ||
        fe(R, function (e, t, n) {
          let r
          if (!n)
            return !0 === e[t]
              ? t.toLowerCase()
              : (r = e.getAttributeNode(t)) && r.specified
              ? r.value
              : null
        }),
      se
    )
  })(C)
  ;(S.find = d),
    (S.expr = d.selectors),
    (S.expr[':'] = S.expr.pseudos),
    (S.uniqueSort = S.unique = d.uniqueSort),
    (S.text = d.getText),
    (S.isXMLDoc = d.isXML),
    (S.contains = d.contains),
    (S.escapeSelector = d.escape)
  const h = function (e, t, n) {
    const r = []
    const i = void 0 !== n
    while ((e = e[t]) && e.nodeType !== 9)
      if (e.nodeType === 1) {
        if (i && S(e).is(n)) break
        r.push(e)
      }
    return r
  }
  const T = function (e, t) {
    for (var n = []; e; e = e.nextSibling)
      e.nodeType === 1 && e !== t && n.push(e)
    return n
  }
  const k = S.expr.match.needsContext
  function A(e, t) {
    return e.nodeName && e.nodeName.toLowerCase() === t.toLowerCase()
  }
  const N = /^<([a-z][^\/\0>:\x20\t\r\n\f]*)[\x20\t\r\n\f]*\/?>(?:<\/\1>|)$/i
  function D(e, n, r) {
    return m(n)
      ? S.grep(e, function (e, t) {
          return !!n.call(e, t, e) !== r
        })
      : n.nodeType
      ? S.grep(e, function (e) {
          return (e === n) !== r
        })
      : typeof n !== 'string'
      ? S.grep(e, function (e) {
          return i.call(n, e) > -1 !== r
        })
      : S.filter(n, e, r)
  }
  ;(S.filter = function (e, t, n) {
    const r = t[0]
    return (
      n && (e = ':not(' + e + ')'),
      t.length === 1 && r.nodeType === 1
        ? S.find.matchesSelector(r, e)
          ? [r]
          : []
        : S.find.matches(
            e,
            S.grep(t, function (e) {
              return e.nodeType === 1
            })
          )
    )
  }),
    S.fn.extend({
      find(e) {
        let t
        let n
        const r = this.length
        const i = this
        if (typeof e !== 'string')
          return this.pushStack(
            S(e).filter(function () {
              for (t = 0; t < r; t++) if (S.contains(i[t], this)) return !0
            })
          )
        for (n = this.pushStack([]), t = 0; t < r; t++) S.find(e, i[t], n)
        return r > 1 ? S.uniqueSort(n) : n
      },
      filter(e) {
        return this.pushStack(D(this, e || [], !1))
      },
      not(e) {
        return this.pushStack(D(this, e || [], !0))
      },
      is(e) {
        return !!D(
          this,
          typeof e === 'string' && k.test(e) ? S(e) : e || [],
          !1
        ).length
      },
    })
  let j
  const q = /^(?:\s*(<[\w\W]+>)[^>]*|#([\w-]+))$/
  ;((S.fn.init = function (e, t, n) {
    let r, i
    if (!e) return this
    if (((n = n || j), typeof e === 'string')) {
      if (
        !(r =
          e[0] === '<' && e[e.length - 1] === '>' && e.length >= 3
            ? [null, e, null]
            : q.exec(e)) ||
        (!r[1] && t)
      )
        return !t || t.jquery ? (t || n).find(e) : this.constructor(t).find(e)
      if (r[1]) {
        if (
          ((t = t instanceof S ? t[0] : t),
          S.merge(
            this,
            S.parseHTML(r[1], t && t.nodeType ? t.ownerDocument || t : E, !0)
          ),
          N.test(r[1]) && S.isPlainObject(t))
        )
          for (r in t) m(this[r]) ? this[r](t[r]) : this.attr(r, t[r])
        return this
      }
      return (
        (i = E.getElementById(r[2])) && ((this[0] = i), (this.length = 1)), this
      )
    }
    return e.nodeType
      ? ((this[0] = e), (this.length = 1), this)
      : m(e)
      ? void 0 !== n.ready
        ? n.ready(e)
        : e(S)
      : S.makeArray(e, this)
  }).prototype = S.fn),
    (j = S(E))
  const L = /^(?:parents|prev(?:Until|All))/
  const H = { children: !0, contents: !0, next: !0, prev: !0 }
  function O(e, t) {
    while ((e = e[t]) && e.nodeType !== 1);
    return e
  }
  S.fn.extend({
    has(e) {
      const t = S(e, this)
      const n = t.length
      return this.filter(function () {
        for (let e = 0; e < n; e++) if (S.contains(this, t[e])) return !0
      })
    },
    closest(e, t) {
      let n
      let r = 0
      const i = this.length
      const o = []
      const a = typeof e !== 'string' && S(e)
      if (!k.test(e))
        for (; r < i; r++)
          for (n = this[r]; n && n !== t; n = n.parentNode)
            if (
              n.nodeType < 11 &&
              (a
                ? a.index(n) > -1
                : n.nodeType === 1 && S.find.matchesSelector(n, e))
            ) {
              o.push(n)
              break
            }
      return this.pushStack(o.length > 1 ? S.uniqueSort(o) : o)
    },
    index(e) {
      return e
        ? typeof e === 'string'
          ? i.call(S(e), this[0])
          : i.call(this, e.jquery ? e[0] : e)
        : this[0] && this[0].parentNode
        ? this.first().prevAll().length
        : -1
    },
    add(e, t) {
      return this.pushStack(S.uniqueSort(S.merge(this.get(), S(e, t))))
    },
    addBack(e) {
      return this.add(e == null ? this.prevObject : this.prevObject.filter(e))
    },
  }),
    S.each(
      {
        parent(e) {
          const t = e.parentNode
          return t && t.nodeType !== 11 ? t : null
        },
        parents(e) {
          return h(e, 'parentNode')
        },
        parentsUntil(e, t, n) {
          return h(e, 'parentNode', n)
        },
        next(e) {
          return O(e, 'nextSibling')
        },
        prev(e) {
          return O(e, 'previousSibling')
        },
        nextAll(e) {
          return h(e, 'nextSibling')
        },
        prevAll(e) {
          return h(e, 'previousSibling')
        },
        nextUntil(e, t, n) {
          return h(e, 'nextSibling', n)
        },
        prevUntil(e, t, n) {
          return h(e, 'previousSibling', n)
        },
        siblings(e) {
          return T((e.parentNode || {}).firstChild, e)
        },
        children(e) {
          return T(e.firstChild)
        },
        contents(e) {
          return e.contentDocument != null && r(e.contentDocument)
            ? e.contentDocument
            : (A(e, 'template') && (e = e.content || e),
              S.merge([], e.childNodes))
        },
      },
      function (r, i) {
        S.fn[r] = function (e, t) {
          let n = S.map(this, i, e)
          return (
            r.slice(-5) !== 'Until' && (t = e),
            t && typeof t === 'string' && (n = S.filter(t, n)),
            this.length > 1 &&
              (H[r] || S.uniqueSort(n), L.test(r) && n.reverse()),
            this.pushStack(n)
          )
        }
      }
    )
  const P = /[^\x20\t\r\n\f]+/g
  function R(e) {
    return e
  }
  function M(e) {
    throw e
  }
  function I(e, t, n, r) {
    let i
    try {
      e && m((i = e.promise))
        ? i.call(e).done(t).fail(n)
        : e && m((i = e.then))
        ? i.call(e, t, n)
        : t.apply(void 0, [e].slice(r))
    } catch (e) {
      n.apply(void 0, [e])
    }
  }
  ;(S.Callbacks = function (r) {
    let e, n
    r =
      typeof r === 'string'
        ? ((e = r),
          (n = {}),
          S.each(e.match(P) || [], function (e, t) {
            n[t] = !0
          }),
          n)
        : S.extend({}, r)
    let i
    let t
    let o
    let a
    let s = []
    let u = []
    let l = -1
    const c = function () {
      for (a = a || r.once, o = i = !0; u.length; l = -1) {
        t = u.shift()
        while (++l < s.length)
          !1 === s[l].apply(t[0], t[1]) &&
            r.stopOnFalse &&
            ((l = s.length), (t = !1))
      }
      r.memory || (t = !1), (i = !1), a && (s = t ? [] : '')
    }
    var f = {
      add() {
        return (
          s &&
            (t && !i && ((l = s.length - 1), u.push(t)),
            (function n(e) {
              S.each(e, function (e, t) {
                m(t)
                  ? (r.unique && f.has(t)) || s.push(t)
                  : t && t.length && w(t) !== 'string' && n(t)
              })
            })(arguments),
            t && !i && c()),
          this
        )
      },
      remove() {
        return (
          S.each(arguments, function (e, t) {
            let n
            while ((n = S.inArray(t, s, n)) > -1) s.splice(n, 1), n <= l && l--
          }),
          this
        )
      },
      has(e) {
        return e ? S.inArray(e, s) > -1 : s.length > 0
      },
      empty() {
        return s && (s = []), this
      },
      disable() {
        return (a = u = []), (s = t = ''), this
      },
      disabled() {
        return !s
      },
      lock() {
        return (a = u = []), t || i || (s = t = ''), this
      },
      locked() {
        return !!a
      },
      fireWith(e, t) {
        return (
          a ||
            ((t = [e, (t = t || []).slice ? t.slice() : t]),
            u.push(t),
            i || c()),
          this
        )
      },
      fire() {
        return f.fireWith(this, arguments), this
      },
      fired() {
        return !!o
      },
    }
    return f
  }),
    S.extend({
      Deferred(e) {
        const o = [
          [
            'notify',
            'progress',
            S.Callbacks('memory'),
            S.Callbacks('memory'),
            2,
          ],
          [
            'resolve',
            'done',
            S.Callbacks('once memory'),
            S.Callbacks('once memory'),
            0,
            'resolved',
          ],
          [
            'reject',
            'fail',
            S.Callbacks('once memory'),
            S.Callbacks('once memory'),
            1,
            'rejected',
          ],
        ]
        let i = 'pending'
        var a = {
          state() {
            return i
          },
          always() {
            return s.done(arguments).fail(arguments), this
          },
          catch(e) {
            return a.then(null, e)
          },
          pipe() {
            let i = arguments
            return S.Deferred(function (r) {
              S.each(o, function (e, t) {
                const n = m(i[t[4]]) && i[t[4]]
                s[t[1]](function () {
                  const e = n && n.apply(this, arguments)
                  e && m(e.promise)
                    ? e
                        .promise()
                        .progress(r.notify)
                        .done(r.resolve)
                        .fail(r.reject)
                    : r[t[0] + 'With'](this, n ? [e] : arguments)
                })
              }),
                (i = null)
            }).promise()
          },
          then(t, n, r) {
            let u = 0
            function l(i, o, a, s) {
              return function () {
                let n = this
                let r = arguments
                const e = function () {
                  let e, t
                  if (!(i < u)) {
                    if ((e = a.apply(n, r)) === o.promise())
                      throw new TypeError('Thenable self-resolution')
                    ;(t =
                      e &&
                      (typeof e === 'object' || typeof e === 'function') &&
                      e.then),
                      m(t)
                        ? s
                          ? t.call(e, l(u, o, R, s), l(u, o, M, s))
                          : (u++,
                            t.call(
                              e,
                              l(u, o, R, s),
                              l(u, o, M, s),
                              l(u, o, R, o.notifyWith)
                            ))
                        : (a !== R && ((n = void 0), (r = [e])),
                          (s || o.resolveWith)(n, r))
                  }
                }
                var t = s
                  ? e
                  : function () {
                      try {
                        e()
                      } catch (e) {
                        S.Deferred.exceptionHook &&
                          S.Deferred.exceptionHook(e, t.stackTrace),
                          u <= i + 1 &&
                            (a !== M && ((n = void 0), (r = [e])),
                            o.rejectWith(n, r))
                      }
                    }
                i
                  ? t()
                  : (S.Deferred.getStackHook &&
                      (t.stackTrace = S.Deferred.getStackHook()),
                    C.setTimeout(t))
              }
            }
            return S.Deferred(function (e) {
              o[0][3].add(l(0, e, m(r) ? r : R, e.notifyWith)),
                o[1][3].add(l(0, e, m(t) ? t : R)),
                o[2][3].add(l(0, e, m(n) ? n : M))
            }).promise()
          },
          promise(e) {
            return e != null ? S.extend(e, a) : a
          },
        }
        var s = {}
        return (
          S.each(o, function (e, t) {
            const n = t[2]
            const r = t[5]
            ;(a[t[1]] = n.add),
              r &&
                n.add(
                  function () {
                    i = r
                  },
                  o[3 - e][2].disable,
                  o[3 - e][3].disable,
                  o[0][2].lock,
                  o[0][3].lock
                ),
              n.add(t[3].fire),
              (s[t[0]] = function () {
                return (
                  s[t[0] + 'With'](this === s ? void 0 : this, arguments), this
                )
              }),
              (s[t[0] + 'With'] = n.fireWith)
          }),
          a.promise(s),
          e && e.call(s, s),
          s
        )
      },
      when(e) {
        let n = arguments.length
        let t = n
        const r = Array(t)
        const i = s.call(arguments)
        const o = S.Deferred()
        const a = function (t) {
          return function (e) {
            ;(r[t] = this),
              (i[t] = arguments.length > 1 ? s.call(arguments) : e),
              --n || o.resolveWith(r, i)
          }
        }
        if (
          n <= 1 &&
          (I(e, o.done(a(t)).resolve, o.reject, !n),
          o.state() === 'pending' || m(i[t] && i[t].then))
        )
          return o.then()
        while (t--) I(i[t], a(t), o.reject)
        return o.promise()
      },
    })
  const W = /^(Eval|Internal|Range|Reference|Syntax|Type|URI)Error$/
  ;(S.Deferred.exceptionHook = function (e, t) {
    C.console &&
      C.console.warn &&
      e &&
      W.test(e.name) &&
      C.console.warn('jQuery.Deferred exception: ' + e.message, e.stack, t)
  }),
    (S.readyException = function (e) {
      C.setTimeout(function () {
        throw e
      })
    })
  const F = S.Deferred()
  function B() {
    E.removeEventListener('DOMContentLoaded', B),
      C.removeEventListener('load', B),
      S.ready()
  }
  ;(S.fn.ready = function (e) {
    return (
      F.then(e).catch(function (e) {
        S.readyException(e)
      }),
      this
    )
  }),
    S.extend({
      isReady: !1,
      readyWait: 1,
      ready(e) {
        ;(!0 === e ? --S.readyWait : S.isReady) ||
          ((S.isReady = !0) !== e && --S.readyWait > 0) ||
          F.resolveWith(E, [S])
      },
    }),
    (S.ready.then = F.then),
    E.readyState === 'complete' ||
    (E.readyState !== 'loading' && !E.documentElement.doScroll)
      ? C.setTimeout(S.ready)
      : (E.addEventListener('DOMContentLoaded', B),
        C.addEventListener('load', B))
  var $ = function (e, t, n, r, i, o, a) {
    let s = 0
    const u = e.length
    let l = n == null
    if (w(n) === 'object') for (s in ((i = !0), n)) $(e, t, s, n[s], !0, o, a)
    else if (
      void 0 !== r &&
      ((i = !0),
      m(r) || (a = !0),
      l &&
        (a
          ? (t.call(e, r), (t = null))
          : ((l = t),
            (t = function (e, t, n) {
              return l.call(S(e), n)
            }))),
      t)
    )
      for (; s < u; s++) t(e[s], n, a ? r : r.call(e[s], s, t(e[s], n)))
    return i ? e : l ? t.call(e) : u ? t(e[0], n) : o
  }
  const _ = /^-ms-/
  const z = /-([a-z])/g
  function U(e, t) {
    return t.toUpperCase()
  }
  function X(e) {
    return e.replace(_, 'ms-').replace(z, U)
  }
  const V = function (e) {
    return e.nodeType === 1 || e.nodeType === 9 || !+e.nodeType
  }
  function G() {
    this.expando = S.expando + G.uid++
  }
  ;(G.uid = 1),
    (G.prototype = {
      cache(e) {
        let t = e[this.expando]
        return (
          t ||
            ((t = {}),
            V(e) &&
              (e.nodeType
                ? (e[this.expando] = t)
                : Object.defineProperty(e, this.expando, {
                    value: t,
                    configurable: !0,
                  }))),
          t
        )
      },
      set(e, t, n) {
        let r
        const i = this.cache(e)
        if (typeof t === 'string') i[X(t)] = n
        else for (r in t) i[X(r)] = t[r]
        return i
      },
      get(e, t) {
        return void 0 === t
          ? this.cache(e)
          : e[this.expando] && e[this.expando][X(t)]
      },
      access(e, t, n) {
        return void 0 === t || (t && typeof t === 'string' && void 0 === n)
          ? this.get(e, t)
          : (this.set(e, t, n), void 0 !== n ? n : t)
      },
      remove(e, t) {
        let n
        const r = e[this.expando]
        if (void 0 !== r) {
          if (void 0 !== t) {
            n = (t = Array.isArray(t)
              ? t.map(X)
              : (t = X(t)) in r
              ? [t]
              : t.match(P) || []).length
            while (n--) delete r[t[n]]
          }
          ;(void 0 === t || S.isEmptyObject(r)) &&
            (e.nodeType ? (e[this.expando] = void 0) : delete e[this.expando])
        }
      },
      hasData(e) {
        const t = e[this.expando]
        return void 0 !== t && !S.isEmptyObject(t)
      },
    })
  const Y = new G()
  const Q = new G()
  const J = /^(?:\{[\w\W]*\}|\[[\w\W]*\])$/
  const K = /[A-Z]/g
  function Z(e, t, n) {
    let r, i
    if (void 0 === n && e.nodeType === 1)
      if (
        ((r = 'data-' + t.replace(K, '-$&').toLowerCase()),
        typeof (n = e.getAttribute(r)) === 'string')
      ) {
        try {
          n =
            (i = n) === 'true' ||
            (i !== 'false' &&
              (i === 'null'
                ? null
                : i === +i + ''
                ? +i
                : J.test(i)
                ? JSON.parse(i)
                : i))
        } catch (e) {}
        Q.set(e, t, n)
      } else n = void 0
    return n
  }
  S.extend({
    hasData(e) {
      return Q.hasData(e) || Y.hasData(e)
    },
    data(e, t, n) {
      return Q.access(e, t, n)
    },
    removeData(e, t) {
      Q.remove(e, t)
    },
    _data(e, t, n) {
      return Y.access(e, t, n)
    },
    _removeData(e, t) {
      Y.remove(e, t)
    },
  }),
    S.fn.extend({
      data(n, e) {
        let t
        let r
        let i
        const o = this[0]
        const a = o && o.attributes
        if (void 0 === n) {
          if (
            this.length &&
            ((i = Q.get(o)), o.nodeType === 1 && !Y.get(o, 'hasDataAttrs'))
          ) {
            t = a.length
            while (t--)
              a[t] &&
                (r = a[t].name).indexOf('data-') === 0 &&
                ((r = X(r.slice(5))), Z(o, r, i[r]))
            Y.set(o, 'hasDataAttrs', !0)
          }
          return i
        }
        return typeof n === 'object'
          ? this.each(function () {
              Q.set(this, n)
            })
          : $(
              this,
              function (e) {
                let t
                if (o && void 0 === e)
                  return void 0 !== (t = Q.get(o, n))
                    ? t
                    : void 0 !== (t = Z(o, n))
                    ? t
                    : void 0
                this.each(function () {
                  Q.set(this, n, e)
                })
              },
              null,
              e,
              arguments.length > 1,
              null,
              !0
            )
      },
      removeData(e) {
        return this.each(function () {
          Q.remove(this, e)
        })
      },
    }),
    S.extend({
      queue(e, t, n) {
        let r
        if (e)
          return (
            (t = (t || 'fx') + 'queue'),
            (r = Y.get(e, t)),
            n &&
              (!r || Array.isArray(n)
                ? (r = Y.access(e, t, S.makeArray(n)))
                : r.push(n)),
            r || []
          )
      },
      dequeue(e, t) {
        t = t || 'fx'
        const n = S.queue(e, t)
        let r = n.length
        let i = n.shift()
        const o = S._queueHooks(e, t)
        i === 'inprogress' && ((i = n.shift()), r--),
          i &&
            (t === 'fx' && n.unshift('inprogress'),
            delete o.stop,
            i.call(
              e,
              function () {
                S.dequeue(e, t)
              },
              o
            )),
          !r && o && o.empty.fire()
      },
      _queueHooks(e, t) {
        const n = t + 'queueHooks'
        return (
          Y.get(e, n) ||
          Y.access(e, n, {
            empty: S.Callbacks('once memory').add(function () {
              Y.remove(e, [t + 'queue', n])
            }),
          })
        )
      },
    }),
    S.fn.extend({
      queue(t, n) {
        let e = 2
        return (
          typeof t !== 'string' && ((n = t), (t = 'fx'), e--),
          arguments.length < e
            ? S.queue(this[0], t)
            : void 0 === n
            ? this
            : this.each(function () {
                const e = S.queue(this, t, n)
                S._queueHooks(this, t),
                  t === 'fx' && e[0] !== 'inprogress' && S.dequeue(this, t)
              })
        )
      },
      dequeue(e) {
        return this.each(function () {
          S.dequeue(this, e)
        })
      },
      clearQueue(e) {
        return this.queue(e || 'fx', [])
      },
      promise(e, t) {
        let n
        let r = 1
        const i = S.Deferred()
        const o = this
        let a = this.length
        const s = function () {
          --r || i.resolveWith(o, [o])
        }
        typeof e !== 'string' && ((t = e), (e = void 0)), (e = e || 'fx')
        while (a--)
          (n = Y.get(o[a], e + 'queueHooks')) &&
            n.empty &&
            (r++, n.empty.add(s))
        return s(), i.promise(t)
      },
    })
  const ee = /[+-]?(?:\d*\.|)\d+(?:[eE][+-]?\d+|)/.source
  const te = new RegExp('^(?:([+-])=|)(' + ee + ')([a-z%]*)$', 'i')
  const ne = ['Top', 'Right', 'Bottom', 'Left']
  const re = E.documentElement
  let ie = function (e) {
    return S.contains(e.ownerDocument, e)
  }
  const oe = { composed: !0 }
  re.getRootNode &&
    (ie = function (e) {
      return (
        S.contains(e.ownerDocument, e) || e.getRootNode(oe) === e.ownerDocument
      )
    })
  const ae = function (e, t) {
    return (
      (e = t || e).style.display === 'none' ||
      (e.style.display === '' && ie(e) && S.css(e, 'display') === 'none')
    )
  }
  function se(e, t, n, r) {
    let i
    let o
    let a = 20
    const s = r
      ? function () {
          return r.cur()
        }
      : function () {
          return S.css(e, t, '')
        }
    let u = s()
    let l = (n && n[3]) || (S.cssNumber[t] ? '' : 'px')
    let c =
      e.nodeType &&
      (S.cssNumber[t] || (l !== 'px' && +u)) &&
      te.exec(S.css(e, t))
    if (c && c[3] !== l) {
      ;(u /= 2), (l = l || c[3]), (c = +u || 1)
      while (a--)
        S.style(e, t, c + l),
          (1 - o) * (1 - (o = s() / u || 0.5)) <= 0 && (a = 0),
          (c /= o)
      ;(c *= 2), S.style(e, t, c + l), (n = n || [])
    }
    return (
      n &&
        ((c = +c || +u || 0),
        (i = n[1] ? c + (n[1] + 1) * n[2] : +n[2]),
        r && ((r.unit = l), (r.start = c), (r.end = i))),
      i
    )
  }
  const ue = {}
  function le(e, t) {
    for (var n, r, i, o, a, s, u, l = [], c = 0, f = e.length; c < f; c++)
      (r = e[c]).style &&
        ((n = r.style.display),
        t
          ? (n === 'none' &&
              ((l[c] = Y.get(r, 'display') || null),
              l[c] || (r.style.display = '')),
            r.style.display === '' &&
              ae(r) &&
              (l[c] =
                ((u = a = o = void 0),
                (a = (i = r).ownerDocument),
                (s = i.nodeName),
                (u = ue[s]) ||
                  ((o = a.body.appendChild(a.createElement(s))),
                  (u = S.css(o, 'display')),
                  o.parentNode.removeChild(o),
                  u === 'none' && (u = 'block'),
                  (ue[s] = u)))))
          : n !== 'none' && ((l[c] = 'none'), Y.set(r, 'display', n)))
    for (c = 0; c < f; c++) l[c] != null && (e[c].style.display = l[c])
    return e
  }
  S.fn.extend({
    show() {
      return le(this, !0)
    },
    hide() {
      return le(this)
    },
    toggle(e) {
      return typeof e === 'boolean'
        ? e
          ? this.show()
          : this.hide()
        : this.each(function () {
            ae(this) ? S(this).show() : S(this).hide()
          })
    },
  })
  let ce
  let fe
  const pe = /^(?:checkbox|radio)$/i
  const de = /<([a-z][^\/\0>\x20\t\r\n\f]*)/i
  const he = /^$|^module$|\/(?:java|ecma)script/i
  ;(ce = E.createDocumentFragment().appendChild(E.createElement('div'))),
    (fe = E.createElement('input')).setAttribute('type', 'radio'),
    fe.setAttribute('checked', 'checked'),
    fe.setAttribute('name', 't'),
    ce.appendChild(fe),
    (y.checkClone = ce.cloneNode(!0).cloneNode(!0).lastChild.checked),
    (ce.innerHTML = '<textarea>x</textarea>'),
    (y.noCloneChecked = !!ce.cloneNode(!0).lastChild.defaultValue),
    (ce.innerHTML = '<option></option>'),
    (y.option = !!ce.lastChild)
  const ge = {
    thead: [1, '<table>', '</table>'],
    col: [2, '<table><colgroup>', '</colgroup></table>'],
    tr: [2, '<table><tbody>', '</tbody></table>'],
    td: [3, '<table><tbody><tr>', '</tr></tbody></table>'],
    _default: [0, '', ''],
  }
  function ve(e, t) {
    let n
    return (
      (n =
        typeof e.getElementsByTagName !== 'undefined'
          ? e.getElementsByTagName(t || '*')
          : typeof e.querySelectorAll !== 'undefined'
          ? e.querySelectorAll(t || '*')
          : []),
      void 0 === t || (t && A(e, t)) ? S.merge([e], n) : n
    )
  }
  function ye(e, t) {
    for (let n = 0, r = e.length; n < r; n++)
      Y.set(e[n], 'globalEval', !t || Y.get(t[n], 'globalEval'))
  }
  ;(ge.tbody = ge.tfoot = ge.colgroup = ge.caption = ge.thead),
    (ge.th = ge.td),
    y.option ||
      (ge.optgroup = ge.option =
        [1, "<select multiple='multiple'>", '</select>'])
  const me = /<|&#?\w+;/
  function xe(e, t, n, r, i) {
    for (
      var o,
        a,
        s,
        u,
        l,
        c,
        f = t.createDocumentFragment(),
        p = [],
        d = 0,
        h = e.length;
      d < h;
      d++
    )
      if ((o = e[d]) || o === 0)
        if (w(o) === 'object') S.merge(p, o.nodeType ? [o] : o)
        else if (me.test(o)) {
          ;(a = a || f.appendChild(t.createElement('div'))),
            (s = (de.exec(o) || ['', ''])[1].toLowerCase()),
            (u = ge[s] || ge._default),
            (a.innerHTML = u[1] + S.htmlPrefilter(o) + u[2]),
            (c = u[0])
          while (c--) a = a.lastChild
          S.merge(p, a.childNodes), ((a = f.firstChild).textContent = '')
        } else p.push(t.createTextNode(o))
    ;(f.textContent = ''), (d = 0)
    while ((o = p[d++]))
      if (r && S.inArray(o, r) > -1) i && i.push(o)
      else if (
        ((l = ie(o)), (a = ve(f.appendChild(o), 'script')), l && ye(a), n)
      ) {
        c = 0
        while ((o = a[c++])) he.test(o.type || '') && n.push(o)
      }
    return f
  }
  const be = /^key/
  const we = /^(?:mouse|pointer|contextmenu|drag|drop)|click/
  const Te = /^([^.]*)(?:\.(.+)|)/
  function Ce() {
    return !0
  }
  function Ee() {
    return !1
  }
  function Se(e, t) {
    return (
      (e ===
        (function () {
          try {
            return E.activeElement
          } catch (e) {}
        })()) ==
      (t === 'focus')
    )
  }
  function ke(e, t, n, r, i, o) {
    let a, s
    if (typeof t === 'object') {
      for (s in (typeof n !== 'string' && ((r = r || n), (n = void 0)), t))
        ke(e, s, n, r, t[s], o)
      return e
    }
    if (
      (r == null && i == null
        ? ((i = n), (r = n = void 0))
        : i == null &&
          (typeof n === 'string'
            ? ((i = r), (r = void 0))
            : ((i = r), (r = n), (n = void 0))),
      !1 === i)
    )
      i = Ee
    else if (!i) return e
    return (
      o === 1 &&
        ((a = i),
        ((i = function (e) {
          return S().off(e), a.apply(this, arguments)
        }).guid = a.guid || (a.guid = S.guid++))),
      e.each(function () {
        S.event.add(this, t, i, r, n)
      })
    )
  }
  function Ae(e, i, o) {
    o
      ? (Y.set(e, i, !1),
        S.event.add(e, i, {
          namespace: !1,
          handler(e) {
            let t
            let n
            let r = Y.get(this, i)
            if (1 & e.isTrigger && this[i]) {
              if (r.length)
                (S.event.special[i] || {}).delegateType && e.stopPropagation()
              else if (
                ((r = s.call(arguments)),
                Y.set(this, i, r),
                (t = o(this, i)),
                this[i](),
                r !== (n = Y.get(this, i)) || t ? Y.set(this, i, !1) : (n = {}),
                r !== n)
              )
                return e.stopImmediatePropagation(), e.preventDefault(), n.value
            } else
              r.length &&
                (Y.set(this, i, {
                  value: S.event.trigger(
                    S.extend(r[0], S.Event.prototype),
                    r.slice(1),
                    this
                  ),
                }),
                e.stopImmediatePropagation())
          },
        }))
      : void 0 === Y.get(e, i) && S.event.add(e, i, Ce)
  }
  ;(S.event = {
    global: {},
    add(t, e, n, r, i) {
      let o
      let a
      let s
      let u
      let l
      let c
      let f
      let p
      let d
      let h
      let g
      const v = Y.get(t)
      if (V(t)) {
        n.handler && ((n = (o = n).handler), (i = o.selector)),
          i && S.find.matchesSelector(re, i),
          n.guid || (n.guid = S.guid++),
          (u = v.events) || (u = v.events = Object.create(null)),
          (a = v.handle) ||
            (a = v.handle =
              function (e) {
                return typeof S !== 'undefined' && S.event.triggered !== e.type
                  ? S.event.dispatch.apply(t, arguments)
                  : void 0
              }),
          (l = (e = (e || '').match(P) || ['']).length)
        while (l--)
          (d = g = (s = Te.exec(e[l]) || [])[1]),
            (h = (s[2] || '').split('.').sort()),
            d &&
              ((f = S.event.special[d] || {}),
              (d = (i ? f.delegateType : f.bindType) || d),
              (f = S.event.special[d] || {}),
              (c = S.extend(
                {
                  type: d,
                  origType: g,
                  data: r,
                  handler: n,
                  guid: n.guid,
                  selector: i,
                  needsContext: i && S.expr.match.needsContext.test(i),
                  namespace: h.join('.'),
                },
                o
              )),
              (p = u[d]) ||
                (((p = u[d] = []).delegateCount = 0),
                (f.setup && !1 !== f.setup.call(t, r, h, a)) ||
                  (t.addEventListener && t.addEventListener(d, a))),
              f.add &&
                (f.add.call(t, c), c.handler.guid || (c.handler.guid = n.guid)),
              i ? p.splice(p.delegateCount++, 0, c) : p.push(c),
              (S.event.global[d] = !0))
      }
    },
    remove(e, t, n, r, i) {
      let o
      let a
      let s
      let u
      let l
      let c
      let f
      let p
      let d
      let h
      let g
      const v = Y.hasData(e) && Y.get(e)
      if (v && (u = v.events)) {
        l = (t = (t || '').match(P) || ['']).length
        while (l--)
          if (
            ((d = g = (s = Te.exec(t[l]) || [])[1]),
            (h = (s[2] || '').split('.').sort()),
            d)
          ) {
            ;(f = S.event.special[d] || {}),
              (p = u[(d = (r ? f.delegateType : f.bindType) || d)] || []),
              (s =
                s[2] &&
                new RegExp('(^|\\.)' + h.join('\\.(?:.*\\.|)') + '(\\.|$)')),
              (a = o = p.length)
            while (o--)
              (c = p[o]),
                (!i && g !== c.origType) ||
                  (n && n.guid !== c.guid) ||
                  (s && !s.test(c.namespace)) ||
                  (r && r !== c.selector && (r !== '**' || !c.selector)) ||
                  (p.splice(o, 1),
                  c.selector && p.delegateCount--,
                  f.remove && f.remove.call(e, c))
            a &&
              !p.length &&
              ((f.teardown && !1 !== f.teardown.call(e, h, v.handle)) ||
                S.removeEvent(e, d, v.handle),
              delete u[d])
          } else for (d in u) S.event.remove(e, d + t[l], n, r, !0)
        S.isEmptyObject(u) && Y.remove(e, 'handle events')
      }
    },
    dispatch(e) {
      let t
      let n
      let r
      let i
      let o
      let a
      const s = new Array(arguments.length)
      const u = S.event.fix(e)
      const l = (Y.get(this, 'events') || Object.create(null))[u.type] || []
      const c = S.event.special[u.type] || {}
      for (s[0] = u, t = 1; t < arguments.length; t++) s[t] = arguments[t]
      if (
        ((u.delegateTarget = this),
        !c.preDispatch || !1 !== c.preDispatch.call(this, u))
      ) {
        ;(a = S.event.handlers.call(this, u, l)), (t = 0)
        while ((i = a[t++]) && !u.isPropagationStopped()) {
          ;(u.currentTarget = i.elem), (n = 0)
          while ((o = i.handlers[n++]) && !u.isImmediatePropagationStopped())
            (u.rnamespace &&
              !1 !== o.namespace &&
              !u.rnamespace.test(o.namespace)) ||
              ((u.handleObj = o),
              (u.data = o.data),
              void 0 !==
                (r = (
                  (S.event.special[o.origType] || {}).handle || o.handler
                ).apply(i.elem, s)) &&
                !1 === (u.result = r) &&
                (u.preventDefault(), u.stopPropagation()))
        }
        return c.postDispatch && c.postDispatch.call(this, u), u.result
      }
    },
    handlers(e, t) {
      let n
      let r
      let i
      let o
      let a
      const s = []
      const u = t.delegateCount
      let l = e.target
      if (u && l.nodeType && !(e.type === 'click' && e.button >= 1))
        for (; l !== this; l = l.parentNode || this)
          if (l.nodeType === 1 && (e.type !== 'click' || !0 !== l.disabled)) {
            for (o = [], a = {}, n = 0; n < u; n++)
              void 0 === a[(i = (r = t[n]).selector + ' ')] &&
                (a[i] = r.needsContext
                  ? S(i, this).index(l) > -1
                  : S.find(i, this, null, [l]).length),
                a[i] && o.push(r)
            o.length && s.push({ elem: l, handlers: o })
          }
      return (
        (l = this), u < t.length && s.push({ elem: l, handlers: t.slice(u) }), s
      )
    },
    addProp(t, e) {
      Object.defineProperty(S.Event.prototype, t, {
        enumerable: !0,
        configurable: !0,
        get: m(e)
          ? function () {
              if (this.originalEvent) return e(this.originalEvent)
            }
          : function () {
              if (this.originalEvent) return this.originalEvent[t]
            },
        set(e) {
          Object.defineProperty(this, t, {
            enumerable: !0,
            configurable: !0,
            writable: !0,
            value: e,
          })
        },
      })
    },
    fix(e) {
      return e[S.expando] ? e : new S.Event(e)
    },
    special: {
      load: { noBubble: !0 },
      click: {
        setup(e) {
          const t = this || e
          return (
            pe.test(t.type) && t.click && A(t, 'input') && Ae(t, 'click', Ce),
            !1
          )
        },
        trigger(e) {
          const t = this || e
          return (
            pe.test(t.type) && t.click && A(t, 'input') && Ae(t, 'click'), !0
          )
        },
        _default(e) {
          const t = e.target
          return (
            (pe.test(t.type) &&
              t.click &&
              A(t, 'input') &&
              Y.get(t, 'click')) ||
            A(t, 'a')
          )
        },
      },
      beforeunload: {
        postDispatch(e) {
          void 0 !== e.result &&
            e.originalEvent &&
            (e.originalEvent.returnValue = e.result)
        },
      },
    },
  }),
    (S.removeEvent = function (e, t, n) {
      e.removeEventListener && e.removeEventListener(t, n)
    }),
    (S.Event = function (e, t) {
      if (!(this instanceof S.Event)) return new S.Event(e, t)
      e && e.type
        ? ((this.originalEvent = e),
          (this.type = e.type),
          (this.isDefaultPrevented =
            e.defaultPrevented ||
            (void 0 === e.defaultPrevented && !1 === e.returnValue)
              ? Ce
              : Ee),
          (this.target =
            e.target && e.target.nodeType === 3
              ? e.target.parentNode
              : e.target),
          (this.currentTarget = e.currentTarget),
          (this.relatedTarget = e.relatedTarget))
        : (this.type = e),
        t && S.extend(this, t),
        (this.timeStamp = (e && e.timeStamp) || Date.now()),
        (this[S.expando] = !0)
    }),
    (S.Event.prototype = {
      constructor: S.Event,
      isDefaultPrevented: Ee,
      isPropagationStopped: Ee,
      isImmediatePropagationStopped: Ee,
      isSimulated: !1,
      preventDefault() {
        const e = this.originalEvent
        ;(this.isDefaultPrevented = Ce),
          e && !this.isSimulated && e.preventDefault()
      },
      stopPropagation() {
        const e = this.originalEvent
        ;(this.isPropagationStopped = Ce),
          e && !this.isSimulated && e.stopPropagation()
      },
      stopImmediatePropagation() {
        const e = this.originalEvent
        ;(this.isImmediatePropagationStopped = Ce),
          e && !this.isSimulated && e.stopImmediatePropagation(),
          this.stopPropagation()
      },
    }),
    S.each(
      {
        altKey: !0,
        bubbles: !0,
        cancelable: !0,
        changedTouches: !0,
        ctrlKey: !0,
        detail: !0,
        eventPhase: !0,
        metaKey: !0,
        pageX: !0,
        pageY: !0,
        shiftKey: !0,
        view: !0,
        char: !0,
        code: !0,
        charCode: !0,
        key: !0,
        keyCode: !0,
        button: !0,
        buttons: !0,
        clientX: !0,
        clientY: !0,
        offsetX: !0,
        offsetY: !0,
        pointerId: !0,
        pointerType: !0,
        screenX: !0,
        screenY: !0,
        targetTouches: !0,
        toElement: !0,
        touches: !0,
        which(e) {
          const t = e.button
          return e.which == null && be.test(e.type)
            ? e.charCode != null
              ? e.charCode
              : e.keyCode
            : !e.which && void 0 !== t && we.test(e.type)
            ? 1 & t
              ? 1
              : 2 & t
              ? 3
              : 4 & t
              ? 2
              : 0
            : e.which
        },
      },
      S.event.addProp
    ),
    S.each({ focus: 'focusin', blur: 'focusout' }, function (e, t) {
      S.event.special[e] = {
        setup() {
          return Ae(this, e, Se), !1
        },
        trigger() {
          return Ae(this, e), !0
        },
        delegateType: t,
      }
    }),
    S.each(
      {
        mouseenter: 'mouseover',
        mouseleave: 'mouseout',
        pointerenter: 'pointerover',
        pointerleave: 'pointerout',
      },
      function (e, i) {
        S.event.special[e] = {
          delegateType: i,
          bindType: i,
          handle(e) {
            let t
            const n = e.relatedTarget
            const r = e.handleObj
            return (
              (n && (n === this || S.contains(this, n))) ||
                ((e.type = r.origType),
                (t = r.handler.apply(this, arguments)),
                (e.type = i)),
              t
            )
          },
        }
      }
    ),
    S.fn.extend({
      on(e, t, n, r) {
        return ke(this, e, t, n, r)
      },
      one(e, t, n, r) {
        return ke(this, e, t, n, r, 1)
      },
      off(e, t, n) {
        let r, i
        if (e && e.preventDefault && e.handleObj)
          return (
            (r = e.handleObj),
            S(e.delegateTarget).off(
              r.namespace ? r.origType + '.' + r.namespace : r.origType,
              r.selector,
              r.handler
            ),
            this
          )
        if (typeof e === 'object') {
          for (i in e) this.off(i, t, e[i])
          return this
        }
        return (
          (!1 !== t && typeof t !== 'function') || ((n = t), (t = void 0)),
          !1 === n && (n = Ee),
          this.each(function () {
            S.event.remove(this, e, n, t)
          })
        )
      },
    })
  const Ne = /<script|<style|<link/i
  const De = /checked\s*(?:[^=]|=\s*.checked.)/i
  const je = /^\s*<!(?:\[CDATA\[|--)|(?:\]\]|--)>\s*$/g
  function qe(e, t) {
    return (
      (A(e, 'table') &&
        A(t.nodeType !== 11 ? t : t.firstChild, 'tr') &&
        S(e).children('tbody')[0]) ||
      e
    )
  }
  function Le(e) {
    return (e.type = (e.getAttribute('type') !== null) + '/' + e.type), e
  }
  function He(e) {
    return (
      (e.type || '').slice(0, 5) === 'true/'
        ? (e.type = e.type.slice(5))
        : e.removeAttribute('type'),
      e
    )
  }
  function Oe(e, t) {
    let n, r, i, o, a, s
    if (t.nodeType === 1) {
      if (Y.hasData(e) && (s = Y.get(e).events))
        for (i in (Y.remove(t, 'handle events'), s))
          for (n = 0, r = s[i].length; n < r; n++) S.event.add(t, i, s[i][n])
      Q.hasData(e) && ((o = Q.access(e)), (a = S.extend({}, o)), Q.set(t, a))
    }
  }
  function Pe(n, r, i, o) {
    r = g(r)
    let e
    let t
    let a
    let s
    let u
    let l
    let c = 0
    const f = n.length
    const p = f - 1
    const d = r[0]
    const h = m(d)
    if (h || (f > 1 && typeof d === 'string' && !y.checkClone && De.test(d)))
      return n.each(function (e) {
        const t = n.eq(e)
        h && (r[0] = d.call(this, e, t.html())), Pe(t, r, i, o)
      })
    if (
      f &&
      ((t = (e = xe(r, n[0].ownerDocument, !1, n, o)).firstChild),
      e.childNodes.length === 1 && (e = t),
      t || o)
    ) {
      for (s = (a = S.map(ve(e, 'script'), Le)).length; c < f; c++)
        (u = e),
          c !== p &&
            ((u = S.clone(u, !0, !0)), s && S.merge(a, ve(u, 'script'))),
          i.call(n[c], u, c)
      if (s)
        for (l = a[a.length - 1].ownerDocument, S.map(a, He), c = 0; c < s; c++)
          (u = a[c]),
            he.test(u.type || '') &&
              !Y.access(u, 'globalEval') &&
              S.contains(l, u) &&
              (u.src && (u.type || '').toLowerCase() !== 'module'
                ? S._evalUrl &&
                  !u.noModule &&
                  S._evalUrl(
                    u.src,
                    { nonce: u.nonce || u.getAttribute('nonce') },
                    l
                  )
                : b(u.textContent.replace(je, ''), u, l))
    }
    return n
  }
  function Re(e, t, n) {
    for (var r, i = t ? S.filter(t, e) : e, o = 0; (r = i[o]) != null; o++)
      n || r.nodeType !== 1 || S.cleanData(ve(r)),
        r.parentNode &&
          (n && ie(r) && ye(ve(r, 'script')), r.parentNode.removeChild(r))
    return e
  }
  S.extend({
    htmlPrefilter(e) {
      return e
    },
    clone(e, t, n) {
      let r
      let i
      let o
      let a
      let s
      let u
      let l
      const c = e.cloneNode(!0)
      const f = ie(e)
      if (
        !(
          y.noCloneChecked ||
          (e.nodeType !== 1 && e.nodeType !== 11) ||
          S.isXMLDoc(e)
        )
      )
        for (a = ve(c), r = 0, i = (o = ve(e)).length; r < i; r++)
          (s = o[r]),
            (u = a[r]),
            void 0,
            (l = u.nodeName.toLowerCase()) === 'input' && pe.test(s.type)
              ? (u.checked = s.checked)
              : (l !== 'input' && l !== 'textarea') ||
                (u.defaultValue = s.defaultValue)
      if (t)
        if (n)
          for (o = o || ve(e), a = a || ve(c), r = 0, i = o.length; r < i; r++)
            Oe(o[r], a[r])
        else Oe(e, c)
      return (a = ve(c, 'script')).length > 0 && ye(a, !f && ve(e, 'script')), c
    },
    cleanData(e) {
      for (var t, n, r, i = S.event.special, o = 0; void 0 !== (n = e[o]); o++)
        if (V(n)) {
          if ((t = n[Y.expando])) {
            if (t.events)
              for (r in t.events)
                i[r] ? S.event.remove(n, r) : S.removeEvent(n, r, t.handle)
            n[Y.expando] = void 0
          }
          n[Q.expando] && (n[Q.expando] = void 0)
        }
    },
  }),
    S.fn.extend({
      detach(e) {
        return Re(this, e, !0)
      },
      remove(e) {
        return Re(this, e)
      },
      text(e) {
        return $(
          this,
          function (e) {
            return void 0 === e
              ? S.text(this)
              : this.empty().each(function () {
                  ;(this.nodeType !== 1 &&
                    this.nodeType !== 11 &&
                    this.nodeType !== 9) ||
                    (this.textContent = e)
                })
          },
          null,
          e,
          arguments.length
        )
      },
      append() {
        return Pe(this, arguments, function (e) {
          ;(this.nodeType !== 1 &&
            this.nodeType !== 11 &&
            this.nodeType !== 9) ||
            qe(this, e).appendChild(e)
        })
      },
      prepend() {
        return Pe(this, arguments, function (e) {
          if (
            this.nodeType === 1 ||
            this.nodeType === 11 ||
            this.nodeType === 9
          ) {
            const t = qe(this, e)
            t.insertBefore(e, t.firstChild)
          }
        })
      },
      before() {
        return Pe(this, arguments, function (e) {
          this.parentNode && this.parentNode.insertBefore(e, this)
        })
      },
      after() {
        return Pe(this, arguments, function (e) {
          this.parentNode && this.parentNode.insertBefore(e, this.nextSibling)
        })
      },
      empty() {
        for (var e, t = 0; (e = this[t]) != null; t++)
          e.nodeType === 1 && (S.cleanData(ve(e, !1)), (e.textContent = ''))
        return this
      },
      clone(e, t) {
        return (
          (e = e != null && e),
          (t = t == null ? e : t),
          this.map(function () {
            return S.clone(this, e, t)
          })
        )
      },
      html(e) {
        return $(
          this,
          function (e) {
            let t = this[0] || {}
            let n = 0
            const r = this.length
            if (void 0 === e && t.nodeType === 1) return t.innerHTML
            if (
              typeof e === 'string' &&
              !Ne.test(e) &&
              !ge[(de.exec(e) || ['', ''])[1].toLowerCase()]
            ) {
              e = S.htmlPrefilter(e)
              try {
                for (; n < r; n++)
                  (t = this[n] || {}).nodeType === 1 &&
                    (S.cleanData(ve(t, !1)), (t.innerHTML = e))
                t = 0
              } catch (e) {}
            }
            t && this.empty().append(e)
          },
          null,
          e,
          arguments.length
        )
      },
      replaceWith() {
        const n = []
        return Pe(
          this,
          arguments,
          function (e) {
            const t = this.parentNode
            S.inArray(this, n) < 0 &&
              (S.cleanData(ve(this)), t && t.replaceChild(e, this))
          },
          n
        )
      },
    }),
    S.each(
      {
        appendTo: 'append',
        prependTo: 'prepend',
        insertBefore: 'before',
        insertAfter: 'after',
        replaceAll: 'replaceWith',
      },
      function (e, a) {
        S.fn[e] = function (e) {
          for (var t, n = [], r = S(e), i = r.length - 1, o = 0; o <= i; o++)
            (t = o === i ? this : this.clone(!0)),
              S(r[o])[a](t),
              u.apply(n, t.get())
          return this.pushStack(n)
        }
      }
    )
  const Me = new RegExp('^(' + ee + ')(?!px)[a-z%]+$', 'i')
  const Ie = function (e) {
    let t = e.ownerDocument.defaultView
    return (t && t.opener) || (t = C), t.getComputedStyle(e)
  }
  const We = function (e, t, n) {
    let r
    let i
    const o = {}
    for (i in t) (o[i] = e.style[i]), (e.style[i] = t[i])
    for (i in ((r = n.call(e)), t)) e.style[i] = o[i]
    return r
  }
  const Fe = new RegExp(ne.join('|'), 'i')
  function Be(e, t, n) {
    let r
    let i
    let o
    let a
    const s = e.style
    return (
      (n = n || Ie(e)) &&
        ((a = n.getPropertyValue(t) || n[t]) !== '' ||
          ie(e) ||
          (a = S.style(e, t)),
        !y.pixelBoxStyles() &&
          Me.test(a) &&
          Fe.test(t) &&
          ((r = s.width),
          (i = s.minWidth),
          (o = s.maxWidth),
          (s.minWidth = s.maxWidth = s.width = a),
          (a = n.width),
          (s.width = r),
          (s.minWidth = i),
          (s.maxWidth = o))),
      void 0 !== a ? a + '' : a
    )
  }
  function $e(e, t) {
    return {
      get() {
        if (!e()) return (this.get = t).apply(this, arguments)
        delete this.get
      },
    }
  }
  !(function () {
    function e() {
      if (l) {
        ;(u.style.cssText =
          'position:absolute;left:-11111px;width:60px;margin-top:1px;padding:0;border:0'),
          (l.style.cssText =
            'position:relative;display:block;box-sizing:border-box;overflow:scroll;margin:auto;border:1px;padding:1px;width:60%;top:1%'),
          re.appendChild(u).appendChild(l)
        const e = C.getComputedStyle(l)
        ;(n = e.top !== '1%'),
          (s = t(e.marginLeft) === 12),
          (l.style.right = '60%'),
          (o = t(e.right) === 36),
          (r = t(e.width) === 36),
          (l.style.position = 'absolute'),
          (i = t(l.offsetWidth / 3) === 12),
          re.removeChild(u),
          (l = null)
      }
    }
    function t(e) {
      return Math.round(parseFloat(e))
    }
    let n
    let r
    let i
    let o
    let a
    let s
    var u = E.createElement('div')
    var l = E.createElement('div')
    l.style &&
      ((l.style.backgroundClip = 'content-box'),
      (l.cloneNode(!0).style.backgroundClip = ''),
      (y.clearCloneStyle = l.style.backgroundClip === 'content-box'),
      S.extend(y, {
        boxSizingReliable() {
          return e(), r
        },
        pixelBoxStyles() {
          return e(), o
        },
        pixelPosition() {
          return e(), n
        },
        reliableMarginLeft() {
          return e(), s
        },
        scrollboxSize() {
          return e(), i
        },
        reliableTrDimensions() {
          let e, t, n, r
          return (
            a == null &&
              ((e = E.createElement('table')),
              (t = E.createElement('tr')),
              (n = E.createElement('div')),
              (e.style.cssText = 'position:absolute;left:-11111px'),
              (t.style.height = '1px'),
              (n.style.height = '9px'),
              re.appendChild(e).appendChild(t).appendChild(n),
              (r = C.getComputedStyle(t)),
              (a = parseInt(r.height) > 3),
              re.removeChild(e)),
            a
          )
        },
      }))
  })()
  const _e = ['Webkit', 'Moz', 'ms']
  const ze = E.createElement('div').style
  const Ue = {}
  function Xe(e) {
    const t = S.cssProps[e] || Ue[e]
    return (
      t ||
      (e in ze
        ? e
        : (Ue[e] =
            (function (e) {
              const t = e[0].toUpperCase() + e.slice(1)
              let n = _e.length
              while (n--) if ((e = _e[n] + t) in ze) return e
            })(e) || e))
    )
  }
  const Ve = /^(none|table(?!-c[ea]).+)/
  const Ge = /^--/
  const Ye = { position: 'absolute', visibility: 'hidden', display: 'block' }
  const Qe = { letterSpacing: '0', fontWeight: '400' }
  function Je(e, t, n) {
    const r = te.exec(t)
    return r ? Math.max(0, r[2] - (n || 0)) + (r[3] || 'px') : t
  }
  function Ke(e, t, n, r, i, o) {
    let a = t === 'width' ? 1 : 0
    let s = 0
    let u = 0
    if (n === (r ? 'border' : 'content')) return 0
    for (; a < 4; a += 2)
      n === 'margin' && (u += S.css(e, n + ne[a], !0, i)),
        r
          ? (n === 'content' && (u -= S.css(e, 'padding' + ne[a], !0, i)),
            n !== 'margin' &&
              (u -= S.css(e, 'border' + ne[a] + 'Width', !0, i)))
          : ((u += S.css(e, 'padding' + ne[a], !0, i)),
            n !== 'padding'
              ? (u += S.css(e, 'border' + ne[a] + 'Width', !0, i))
              : (s += S.css(e, 'border' + ne[a] + 'Width', !0, i)))
    return (
      !r &&
        o >= 0 &&
        (u +=
          Math.max(
            0,
            Math.ceil(
              e['offset' + t[0].toUpperCase() + t.slice(1)] - o - u - s - 0.5
            )
          ) || 0),
      u
    )
  }
  function Ze(e, t, n) {
    const r = Ie(e)
    let i =
      (!y.boxSizingReliable() || n) &&
      S.css(e, 'boxSizing', !1, r) === 'border-box'
    let o = i
    let a = Be(e, t, r)
    const s = 'offset' + t[0].toUpperCase() + t.slice(1)
    if (Me.test(a)) {
      if (!n) return a
      a = 'auto'
    }
    return (
      ((!y.boxSizingReliable() && i) ||
        (!y.reliableTrDimensions() && A(e, 'tr')) ||
        a === 'auto' ||
        (!parseFloat(a) && S.css(e, 'display', !1, r) === 'inline')) &&
        e.getClientRects().length &&
        ((i = S.css(e, 'boxSizing', !1, r) === 'border-box'),
        (o = s in e) && (a = e[s])),
      (a = parseFloat(a) || 0) +
        Ke(e, t, n || (i ? 'border' : 'content'), o, r, a) +
        'px'
    )
  }
  function et(e, t, n, r, i) {
    return new et.prototype.init(e, t, n, r, i)
  }
  S.extend({
    cssHooks: {
      opacity: {
        get(e, t) {
          if (t) {
            const n = Be(e, 'opacity')
            return n === '' ? '1' : n
          }
        },
      },
    },
    cssNumber: {
      animationIterationCount: !0,
      columnCount: !0,
      fillOpacity: !0,
      flexGrow: !0,
      flexShrink: !0,
      fontWeight: !0,
      gridArea: !0,
      gridColumn: !0,
      gridColumnEnd: !0,
      gridColumnStart: !0,
      gridRow: !0,
      gridRowEnd: !0,
      gridRowStart: !0,
      lineHeight: !0,
      opacity: !0,
      order: !0,
      orphans: !0,
      widows: !0,
      zIndex: !0,
      zoom: !0,
    },
    cssProps: {},
    style(e, t, n, r) {
      if (e && e.nodeType !== 3 && e.nodeType !== 8 && e.style) {
        let i
        let o
        let a
        const s = X(t)
        const u = Ge.test(t)
        const l = e.style
        if (
          (u || (t = Xe(s)), (a = S.cssHooks[t] || S.cssHooks[s]), void 0 === n)
        )
          return (
            a && 'get' in a && void 0 !== (i = a.get(e, !1, r))
              ? i
              : l[t]((o = typeof n)) === 'string' &&
                (i = te.exec(n)) &&
                i[1] &&
                ((n = se(e, t, i)), (o = 'number')),
            n != null &&
              n == n &&
              (o !== 'number' ||
                u ||
                (n += (i && i[3]) || (S.cssNumber[s] ? '' : 'px')),
              y.clearCloneStyle ||
                n !== '' ||
                t.indexOf('background') !== 0 ||
                (l[t] = 'inherit'),
              (a && 'set' in a && void 0 === (n = a.set(e, n, r))) ||
                (u ? l.setProperty(t, n) : (l[t] = n)))
          )
      }
    },
    css(e, t, n, r) {
      let i
      let o
      let a
      const s = X(t)
      return (
        Ge.test(t) || (t = Xe(s)),
        (a = S.cssHooks[t] || S.cssHooks[s]) &&
          'get' in a &&
          (i = a.get(e, !0, n)),
        void 0 === i && (i = Be(e, t, r)),
        i === 'normal' && t in Qe && (i = Qe[t]),
        n === '' || n
          ? ((o = parseFloat(i)), !0 === n || isFinite(o) ? o || 0 : i)
          : i
      )
    },
  }),
    S.each(['height', 'width'], function (e, u) {
      S.cssHooks[u] = {
        get(e, t, n) {
          if (t)
            return !Ve.test(S.css(e, 'display')) ||
              (e.getClientRects().length && e.getBoundingClientRect().width)
              ? Ze(e, u, n)
              : We(e, Ye, function () {
                  return Ze(e, u, n)
                })
        },
        set(e, t, n) {
          let r
          const i = Ie(e)
          const o = !y.scrollboxSize() && i.position === 'absolute'
          const a = (o || n) && S.css(e, 'boxSizing', !1, i) === 'border-box'
          let s = n ? Ke(e, u, n, a, i) : 0
          return (
            a &&
              o &&
              (s -= Math.ceil(
                e['offset' + u[0].toUpperCase() + u.slice(1)] -
                  parseFloat(i[u]) -
                  Ke(e, u, 'border', !1, i) -
                  0.5
              )),
            s &&
              (r = te.exec(t)) &&
              (r[3] || 'px') !== 'px' &&
              ((e.style[u] = t), (t = S.css(e, u))),
            Je(0, t, s)
          )
        },
      }
    }),
    (S.cssHooks.marginLeft = $e(y.reliableMarginLeft, function (e, t) {
      if (t)
        return (
          (parseFloat(Be(e, 'marginLeft')) ||
            e.getBoundingClientRect().left -
              We(e, { marginLeft: 0 }, function () {
                return e.getBoundingClientRect().left
              })) + 'px'
        )
    })),
    S.each({ margin: '', padding: '', border: 'Width' }, function (i, o) {
      ;(S.cssHooks[i + o] = {
        expand(e) {
          for (
            var t = 0, n = {}, r = typeof e === 'string' ? e.split(' ') : [e];
            t < 4;
            t++
          )
            n[i + ne[t] + o] = r[t] || r[t - 2] || r[0]
          return n
        },
      }),
        i !== 'margin' && (S.cssHooks[i + o].set = Je)
    }),
    S.fn.extend({
      css(e, t) {
        return $(
          this,
          function (e, t, n) {
            let r
            let i
            const o = {}
            let a = 0
            if (Array.isArray(t)) {
              for (r = Ie(e), i = t.length; a < i; a++)
                o[t[a]] = S.css(e, t[a], !1, r)
              return o
            }
            return void 0 !== n ? S.style(e, t, n) : S.css(e, t)
          },
          e,
          t,
          arguments.length > 1
        )
      },
    }),
    (((S.Tween = et).prototype = {
      constructor: et,
      init(e, t, n, r, i, o) {
        ;(this.elem = e),
          (this.prop = n),
          (this.easing = i || S.easing._default),
          (this.options = t),
          (this.start = this.now = this.cur()),
          (this.end = r),
          (this.unit = o || (S.cssNumber[n] ? '' : 'px'))
      },
      cur() {
        const e = et.propHooks[this.prop]
        return e && e.get ? e.get(this) : et.propHooks._default.get(this)
      },
      run(e) {
        let t
        const n = et.propHooks[this.prop]
        return (
          this.options.duration
            ? (this.pos = t =
                S.easing[this.easing](
                  e,
                  this.options.duration * e,
                  0,
                  1,
                  this.options.duration
                ))
            : (this.pos = t = e),
          (this.now = (this.end - this.start) * t + this.start),
          this.options.step &&
            this.options.step.call(this.elem, this.now, this),
          n && n.set ? n.set(this) : et.propHooks._default.set(this),
          this
        )
      },
    }).init.prototype = et.prototype),
    ((et.propHooks = {
      _default: {
        get(e) {
          let t
          return e.elem.nodeType !== 1 ||
            (e.elem[e.prop] != null && e.elem.style[e.prop] == null)
            ? e.elem[e.prop]
            : (t = S.css(e.elem, e.prop, '')) && t !== 'auto'
            ? t
            : 0
        },
        set(e) {
          S.fx.step[e.prop]
            ? S.fx.step[e.prop](e)
            : e.elem.nodeType !== 1 ||
              (!S.cssHooks[e.prop] && e.elem.style[Xe(e.prop)] == null)
            ? (e.elem[e.prop] = e.now)
            : S.style(e.elem, e.prop, e.now + e.unit)
        },
      },
    }).scrollTop = et.propHooks.scrollLeft =
      {
        set(e) {
          e.elem.nodeType && e.elem.parentNode && (e.elem[e.prop] = e.now)
        },
      }),
    (S.easing = {
      linear(e) {
        return e
      },
      swing(e) {
        return 0.5 - Math.cos(e * Math.PI) / 2
      },
      _default: 'swing',
    }),
    (S.fx = et.prototype.init),
    (S.fx.step = {})
  let tt
  let nt
  let rt
  let it
  const ot = /^(?:toggle|show|hide)$/
  const at = /queueHooks$/
  function st() {
    nt &&
      (!1 === E.hidden && C.requestAnimationFrame
        ? C.requestAnimationFrame(st)
        : C.setTimeout(st, S.fx.interval),
      S.fx.tick())
  }
  function ut() {
    return (
      C.setTimeout(function () {
        tt = void 0
      }),
      (tt = Date.now())
    )
  }
  function lt(e, t) {
    let n
    let r = 0
    const i = { height: e }
    for (t = t ? 1 : 0; r < 4; r += 2 - t)
      i['margin' + (n = ne[r])] = i['padding' + n] = e
    return t && (i.opacity = i.width = e), i
  }
  function ct(e, t, n) {
    for (
      var r,
        i = (ft.tweeners[t] || []).concat(ft.tweeners['*']),
        o = 0,
        a = i.length;
      o < a;
      o++
    )
      if ((r = i[o].call(n, t, e))) return r
  }
  function ft(o, e, t) {
    let n
    let a
    let r = 0
    const i = ft.prefilters.length
    const s = S.Deferred().always(function () {
      delete u.elem
    })
    var u = function () {
      if (a) return !1
      for (
        var e = tt || ut(),
          t = Math.max(0, l.startTime + l.duration - e),
          n = 1 - (t / l.duration || 0),
          r = 0,
          i = l.tweens.length;
        r < i;
        r++
      )
        l.tweens[r].run(n)
      return (
        s.notifyWith(o, [l, n, t]),
        n < 1 && i
          ? t
          : (i || s.notifyWith(o, [l, 1, 0]), s.resolveWith(o, [l]), !1)
      )
    }
    var l = s.promise({
      elem: o,
      props: S.extend({}, e),
      opts: S.extend(!0, { specialEasing: {}, easing: S.easing._default }, t),
      originalProperties: e,
      originalOptions: t,
      startTime: tt || ut(),
      duration: t.duration,
      tweens: [],
      createTween(e, t) {
        const n = S.Tween(
          o,
          l.opts,
          e,
          t,
          l.opts.specialEasing[e] || l.opts.easing
        )
        return l.tweens.push(n), n
      },
      stop(e) {
        let t = 0
        const n = e ? l.tweens.length : 0
        if (a) return this
        for (a = !0; t < n; t++) l.tweens[t].run(1)
        return (
          e
            ? (s.notifyWith(o, [l, 1, 0]), s.resolveWith(o, [l, e]))
            : s.rejectWith(o, [l, e]),
          this
        )
      },
    })
    const c = l.props
    for (
      !(function (e, t) {
        let n, r, i, o, a
        for (n in e)
          if (
            ((i = t[(r = X(n))]),
            (o = e[n]),
            Array.isArray(o) && ((i = o[1]), (o = e[n] = o[0])),
            n !== r && ((e[r] = o), delete e[n]),
            (a = S.cssHooks[r]) && ('expand' in a))
          )
            for (n in ((o = a.expand(o)), delete e[r], o))
              (n in e) || ((e[n] = o[n]), (t[n] = i))
          else t[r] = i
      })(c, l.opts.specialEasing);
      r < i;
      r++
    )
      if ((n = ft.prefilters[r].call(l, o, c, l.opts)))
        return (
          m(n.stop) &&
            (S._queueHooks(l.elem, l.opts.queue).stop = n.stop.bind(n)),
          n
        )
    return (
      S.map(c, ct, l),
      m(l.opts.start) && l.opts.start.call(o, l),
      l
        .progress(l.opts.progress)
        .done(l.opts.done, l.opts.complete)
        .fail(l.opts.fail)
        .always(l.opts.always),
      S.fx.timer(S.extend(u, { elem: o, anim: l, queue: l.opts.queue })),
      l
    )
  }
  ;(S.Animation = S.extend(ft, {
    tweeners: {
      '*': [
        function (e, t) {
          const n = this.createTween(e, t)
          return se(n.elem, e, te.exec(t), n), n
        },
      ],
    },
    tweener(e, t) {
      m(e) ? ((t = e), (e = ['*'])) : (e = e.match(P))
      for (var n, r = 0, i = e.length; r < i; r++)
        (n = e[r]),
          (ft.tweeners[n] = ft.tweeners[n] || []),
          ft.tweeners[n].unshift(t)
    },
    prefilters: [
      function (e, t, n) {
        let r
        let i
        let o
        let a
        let s
        let u
        let l
        let c
        const f = 'width' in t || 'height' in t
        const p = this
        const d = {}
        const h = e.style
        let g = e.nodeType && ae(e)
        let v = Y.get(e, 'fxshow')
        for (r in (n.queue ||
          ((a = S._queueHooks(e, 'fx')).unqueued == null &&
            ((a.unqueued = 0),
            (s = a.empty.fire),
            (a.empty.fire = function () {
              a.unqueued || s()
            })),
          a.unqueued++,
          p.always(function () {
            p.always(function () {
              a.unqueued--, S.queue(e, 'fx').length || a.empty.fire()
            })
          })),
        t))
          if (((i = t[r]), ot.test(i))) {
            if (
              (delete t[r],
              (o = o || i === 'toggle'),
              i === (g ? 'hide' : 'show'))
            ) {
              if (i !== 'show' || !v || void 0 === v[r]) continue
              g = !0
            }
            d[r] = (v && v[r]) || S.style(e, r)
          }
        if ((u = !S.isEmptyObject(t)) || !S.isEmptyObject(d))
          for (r in (f &&
            e.nodeType === 1 &&
            ((n.overflow = [h.overflow, h.overflowX, h.overflowY]),
            (l = v && v.display) == null && (l = Y.get(e, 'display')),
            (c = S.css(e, 'display')) === 'none' &&
              (l
                ? (c = l)
                : (le([e], !0),
                  (l = e.style.display || l),
                  (c = S.css(e, 'display')),
                  le([e]))),
            (c === 'inline' || (c === 'inline-block' && l != null)) &&
              S.css(e, 'float') === 'none' &&
              (u ||
                (p.done(function () {
                  h.display = l
                }),
                l == null && ((c = h.display), (l = c === 'none' ? '' : c))),
              (h.display = 'inline-block'))),
          n.overflow &&
            ((h.overflow = 'hidden'),
            p.always(function () {
              ;(h.overflow = n.overflow[0]),
                (h.overflowX = n.overflow[1]),
                (h.overflowY = n.overflow[2])
            })),
          (u = !1),
          d))
            u ||
              (v
                ? 'hidden' in v && (g = v.hidden)
                : (v = Y.access(e, 'fxshow', { display: l })),
              o && (v.hidden = !g),
              g && le([e], !0),
              p.done(function () {
                for (r in (g || le([e]), Y.remove(e, 'fxshow'), d))
                  S.style(e, r, d[r])
              })),
              (u = ct(g ? v[r] : 0, r, p)),
              r in v ||
                ((v[r] = u.start), g && ((u.end = u.start), (u.start = 0)))
      },
    ],
    prefilter(e, t) {
      t ? ft.prefilters.unshift(e) : ft.prefilters.push(e)
    },
  })),
    (S.speed = function (e, t, n) {
      const r =
        e && typeof e === 'object'
          ? S.extend({}, e)
          : {
              complete: n || (!n && t) || (m(e) && e),
              duration: e,
              easing: (n && t) || (t && !m(t) && t),
            }
      return (
        S.fx.off
          ? (r.duration = 0)
          : typeof r.duration !== 'number' &&
            (r.duration in S.fx.speeds
              ? (r.duration = S.fx.speeds[r.duration])
              : (r.duration = S.fx.speeds._default)),
        (r.queue != null && !0 !== r.queue) || (r.queue = 'fx'),
        (r.old = r.complete),
        (r.complete = function () {
          m(r.old) && r.old.call(this), r.queue && S.dequeue(this, r.queue)
        }),
        r
      )
    }),
    S.fn.extend({
      fadeTo(e, t, n, r) {
        return this.filter(ae)
          .css('opacity', 0)
          .show()
          .end()
          .animate({ opacity: t }, e, n, r)
      },
      animate(t, e, n, r) {
        const i = S.isEmptyObject(t)
        const o = S.speed(e, n, r)
        const a = function () {
          const e = ft(this, S.extend({}, t), o)
          ;(i || Y.get(this, 'finish')) && e.stop(!0)
        }
        return (
          (a.finish = a),
          i || !1 === o.queue ? this.each(a) : this.queue(o.queue, a)
        )
      },
      stop(i, e, o) {
        const a = function (e) {
          const t = e.stop
          delete e.stop, t(o)
        }
        return (
          typeof i !== 'string' && ((o = e), (e = i), (i = void 0)),
          e && this.queue(i || 'fx', []),
          this.each(function () {
            let e = !0
            let t = i != null && i + 'queueHooks'
            const n = S.timers
            const r = Y.get(this)
            if (t) r[t] && r[t].stop && a(r[t])
            else for (t in r) r[t] && r[t].stop && at.test(t) && a(r[t])
            for (t = n.length; t--; )
              n[t].elem !== this ||
                (i != null && n[t].queue !== i) ||
                (n[t].anim.stop(o), (e = !1), n.splice(t, 1))
            ;(!e && o) || S.dequeue(this, i)
          })
        )
      },
      finish(a) {
        return (
          !1 !== a && (a = a || 'fx'),
          this.each(function () {
            let e
            const t = Y.get(this)
            const n = t[a + 'queue']
            const r = t[a + 'queueHooks']
            const i = S.timers
            const o = n ? n.length : 0
            for (
              t.finish = !0,
                S.queue(this, a, []),
                r && r.stop && r.stop.call(this, !0),
                e = i.length;
              e--;

            )
              i[e].elem === this &&
                i[e].queue === a &&
                (i[e].anim.stop(!0), i.splice(e, 1))
            for (e = 0; e < o; e++)
              n[e] && n[e].finish && n[e].finish.call(this)
            delete t.finish
          })
        )
      },
    }),
    S.each(['toggle', 'show', 'hide'], function (e, r) {
      const i = S.fn[r]
      S.fn[r] = function (e, t, n) {
        return e == null || typeof e === 'boolean'
          ? i.apply(this, arguments)
          : this.animate(lt(r, !0), e, t, n)
      }
    }),
    S.each(
      {
        slideDown: lt('show'),
        slideUp: lt('hide'),
        slideToggle: lt('toggle'),
        fadeIn: { opacity: 'show' },
        fadeOut: { opacity: 'hide' },
        fadeToggle: { opacity: 'toggle' },
      },
      function (e, r) {
        S.fn[e] = function (e, t, n) {
          return this.animate(r, e, t, n)
        }
      }
    ),
    (S.timers = []),
    (S.fx.tick = function () {
      let e
      let t = 0
      const n = S.timers
      for (tt = Date.now(); t < n.length; t++)
        (e = n[t])() || n[t] !== e || n.splice(t--, 1)
      n.length || S.fx.stop(), (tt = void 0)
    }),
    (S.fx.timer = function (e) {
      S.timers.push(e), S.fx.start()
    }),
    (S.fx.interval = 13),
    (S.fx.start = function () {
      nt || ((nt = !0), st())
    }),
    (S.fx.stop = function () {
      nt = null
    }),
    (S.fx.speeds = { slow: 600, fast: 200, _default: 400 }),
    (S.fn.delay = function (r, e) {
      return (
        (r = (S.fx && S.fx.speeds[r]) || r),
        (e = e || 'fx'),
        this.queue(e, function (e, t) {
          const n = C.setTimeout(e, r)
          t.stop = function () {
            C.clearTimeout(n)
          }
        })
      )
    }),
    (rt = E.createElement('input')),
    (it = E.createElement('select').appendChild(E.createElement('option'))),
    (rt.type = 'checkbox'),
    (y.checkOn = rt.value !== ''),
    (y.optSelected = it.selected),
    ((rt = E.createElement('input')).value = 't'),
    (rt.type = 'radio'),
    (y.radioValue = rt.value === 't')
  let pt
  const dt = S.expr.attrHandle
  S.fn.extend({
    attr(e, t) {
      return $(this, S.attr, e, t, arguments.length > 1)
    },
    removeAttr(e) {
      return this.each(function () {
        S.removeAttr(this, e)
      })
    },
  }),
    S.extend({
      attr(e, t, n) {
        let r
        let i
        const o = e.nodeType
        if (o !== 3 && o !== 8 && o !== 2)
          return typeof e.getAttribute === 'undefined'
            ? S.prop(e, t, n)
            : ((o === 1 && S.isXMLDoc(e)) ||
                (i =
                  S.attrHooks[t.toLowerCase()] ||
                  (S.expr.match.bool.test(t) ? pt : void 0)),
              void 0 !== n
                ? n === null
                  ? void S.removeAttr(e, t)
                  : i && 'set' in i && void 0 !== (r = i.set(e, n, t))
                  ? r
                  : (e.setAttribute(t, n + ''), n)
                : i && 'get' in i && (r = i.get(e, t)) !== null
                ? r
                : (r = S.find.attr(e, t)) == null
                ? void 0
                : r)
      },
      attrHooks: {
        type: {
          set(e, t) {
            if (!y.radioValue && t === 'radio' && A(e, 'input')) {
              const n = e.value
              return e.setAttribute('type', t), n && (e.value = n), t
            }
          },
        },
      },
      removeAttr(e, t) {
        let n
        let r = 0
        const i = t && t.match(P)
        if (i && e.nodeType === 1) while ((n = i[r++])) e.removeAttribute(n)
      },
    }),
    (pt = {
      set(e, t, n) {
        return !1 === t ? S.removeAttr(e, n) : e.setAttribute(n, n), n
      },
    }),
    S.each(S.expr.match.bool.source.match(/\w+/g), function (e, t) {
      const a = dt[t] || S.find.attr
      dt[t] = function (e, t, n) {
        let r
        let i
        const o = t.toLowerCase()
        return (
          n ||
            ((i = dt[o]),
            (dt[o] = r),
            (r = a(e, t, n) != null ? o : null),
            (dt[o] = i)),
          r
        )
      }
    })
  const ht = /^(?:input|select|textarea|button)$/i
  const gt = /^(?:a|area)$/i
  function vt(e) {
    return (e.match(P) || []).join(' ')
  }
  function yt(e) {
    return (e.getAttribute && e.getAttribute('class')) || ''
  }
  function mt(e) {
    return Array.isArray(e) ? e : (typeof e === 'string' && e.match(P)) || []
  }
  S.fn.extend({
    prop(e, t) {
      return $(this, S.prop, e, t, arguments.length > 1)
    },
    removeProp(e) {
      return this.each(function () {
        delete this[S.propFix[e] || e]
      })
    },
  }),
    S.extend({
      prop(e, t, n) {
        let r
        let i
        const o = e.nodeType
        if (o !== 3 && o !== 8 && o !== 2)
          return (
            (o === 1 && S.isXMLDoc(e)) ||
              ((t = S.propFix[t] || t), (i = S.propHooks[t])),
            void 0 !== n
              ? i && 'set' in i && void 0 !== (r = i.set(e, n, t))
                ? r
                : (e[t] = n)
              : i && 'get' in i && (r = i.get(e, t)) !== null
              ? r
              : e[t]
          )
      },
      propHooks: {
        tabIndex: {
          get(e) {
            const t = S.find.attr(e, 'tabindex')
            return t
              ? parseInt(t, 10)
              : ht.test(e.nodeName) || (gt.test(e.nodeName) && e.href)
              ? 0
              : -1
          },
        },
      },
      propFix: { for: 'htmlFor', class: 'className' },
    }),
    y.optSelected ||
      (S.propHooks.selected = {
        get(e) {
          const t = e.parentNode
          return t && t.parentNode && t.parentNode.selectedIndex, null
        },
        set(e) {
          const t = e.parentNode
          t && (t.selectedIndex, t.parentNode && t.parentNode.selectedIndex)
        },
      }),
    S.each(
      [
        'tabIndex',
        'readOnly',
        'maxLength',
        'cellSpacing',
        'cellPadding',
        'rowSpan',
        'colSpan',
        'useMap',
        'frameBorder',
        'contentEditable',
      ],
      function () {
        S.propFix[this.toLowerCase()] = this
      }
    ),
    S.fn.extend({
      addClass(t) {
        let e
        let n
        let r
        let i
        let o
        let a
        let s
        let u = 0
        if (m(t))
          return this.each(function (e) {
            S(this).addClass(t.call(this, e, yt(this)))
          })
        if ((e = mt(t)).length)
          while ((n = this[u++]))
            if (((i = yt(n)), (r = n.nodeType === 1 && ' ' + vt(i) + ' '))) {
              a = 0
              while ((o = e[a++])) !r.includes(' ' + o + ' ') && (r += o + ' ')
              i !== (s = vt(r)) && n.setAttribute('class', s)
            }
        return this
      },
      removeClass(t) {
        let e
        let n
        let r
        let i
        let o
        let a
        let s
        let u = 0
        if (m(t))
          return this.each(function (e) {
            S(this).removeClass(t.call(this, e, yt(this)))
          })
        if (!arguments.length) return this.attr('class', '')
        if ((e = mt(t)).length)
          while ((n = this[u++]))
            if (((i = yt(n)), (r = n.nodeType === 1 && ' ' + vt(i) + ' '))) {
              a = 0
              while ((o = e[a++]))
                while (r.includes(' ' + o + ' '))
                  r = r.replace(' ' + o + ' ', ' ')
              i !== (s = vt(r)) && n.setAttribute('class', s)
            }
        return this
      },
      toggleClass(i, t) {
        const o = typeof i
        const a = o === 'string' || Array.isArray(i)
        return typeof t === 'boolean' && a
          ? t
            ? this.addClass(i)
            : this.removeClass(i)
          : m(i)
          ? this.each(function (e) {
              S(this).toggleClass(i.call(this, e, yt(this), t), t)
            })
          : this.each(function () {
              let e, t, n, r
              if (a) {
                ;(t = 0), (n = S(this)), (r = mt(i))
                while ((e = r[t++]))
                  n.hasClass(e) ? n.removeClass(e) : n.addClass(e)
              } else (void 0 !== i && o !== 'boolean') || ((e = yt(this)) && Y.set(this, '__className__', e), this.setAttribute && this.setAttribute('class', e || !1 === i ? '' : Y.get(this, '__className__') || ''))
            })
      },
      hasClass(e) {
        let t
        let n
        let r = 0
        t = ' ' + e + ' '
        while ((n = this[r++]))
          if (n.nodeType === 1 && (' ' + vt(yt(n)) + ' ').includes(t)) return !0
        return !1
      },
    })
  const xt = /\r/g
  S.fn.extend({
    val(n) {
      let r
      let e
      let i
      const t = this[0]
      return arguments.length
        ? ((i = m(n)),
          this.each(function (e) {
            let t
            this.nodeType === 1 &&
              ((t = i ? n.call(this, e, S(this).val()) : n) == null
                ? (t = '')
                : typeof t === 'number'
                ? (t += '')
                : Array.isArray(t) &&
                  (t = S.map(t, function (e) {
                    return e == null ? '' : e + ''
                  })),
              ((r =
                S.valHooks[this.type] ||
                S.valHooks[this.nodeName.toLowerCase()]) &&
                'set' in r &&
                void 0 !== r.set(this, t, 'value')) ||
                (this.value = t))
          }))
        : t
        ? (r = S.valHooks[t.type] || S.valHooks[t.nodeName.toLowerCase()]) &&
          'get' in r &&
          void 0 !== (e = r.get(t, 'value'))
          ? e
          : typeof (e = t.value) === 'string'
          ? e.replace(xt, '')
          : e == null
          ? ''
          : e
        : void 0
    },
  }),
    S.extend({
      valHooks: {
        option: {
          get(e) {
            const t = S.find.attr(e, 'value')
            return t != null ? t : vt(S.text(e))
          },
        },
        select: {
          get(e) {
            let t
            let n
            let r
            const i = e.options
            const o = e.selectedIndex
            const a = e.type === 'select-one'
            const s = a ? null : []
            const u = a ? o + 1 : i.length
            for (r = o < 0 ? u : a ? o : 0; r < u; r++)
              if (
                ((n = i[r]).selected || r === o) &&
                !n.disabled &&
                (!n.parentNode.disabled || !A(n.parentNode, 'optgroup'))
              ) {
                if (((t = S(n).val()), a)) return t
                s.push(t)
              }
            return s
          },
          set(e, t) {
            let n
            let r
            const i = e.options
            const o = S.makeArray(t)
            let a = i.length
            while (a--)
              ((r = i[a]).selected =
                S.inArray(S.valHooks.option.get(r), o) > -1) && (n = !0)
            return n || (e.selectedIndex = -1), o
          },
        },
      },
    }),
    S.each(['radio', 'checkbox'], function () {
      ;(S.valHooks[this] = {
        set(e, t) {
          if (Array.isArray(t))
            return (e.checked = S.inArray(S(e).val(), t) > -1)
        },
      }),
        y.checkOn ||
          (S.valHooks[this].get = function (e) {
            return e.getAttribute('value') === null ? 'on' : e.value
          })
    }),
    (y.focusin = 'onfocusin' in C)
  const bt = /^(?:focusinfocus|focusoutblur)$/
  const wt = function (e) {
    e.stopPropagation()
  }
  S.extend(S.event, {
    trigger(e, t, n, r) {
      let i
      let o
      let a
      let s
      let u
      let l
      let c
      let f
      const p = [n || E]
      let d = v.call(e, 'type') ? e.type : e
      let h = v.call(e, 'namespace') ? e.namespace.split('.') : []
      if (
        ((o = f = a = n = n || E),
        n.nodeType !== 3 &&
          n.nodeType !== 8 &&
          !bt.test(d + S.event.triggered) &&
          (d.includes('.') && ((d = (h = d.split('.')).shift()), h.sort()),
          (u = !d.includes(':') && 'on' + d),
          ((e = e[S.expando]
            ? e
            : new S.Event(d, typeof e === 'object' && e)).isTrigger = r
            ? 2
            : 3),
          (e.namespace = h.join('.')),
          (e.rnamespace = e.namespace
            ? new RegExp('(^|\\.)' + h.join('\\.(?:.*\\.|)') + '(\\.|$)')
            : null),
          (e.result = void 0),
          e.target || (e.target = n),
          (t = t == null ? [e] : S.makeArray(t, [e])),
          (c = S.event.special[d] || {}),
          r || !c.trigger || !1 !== c.trigger.apply(n, t)))
      ) {
        if (!r && !c.noBubble && !x(n)) {
          for (
            s = c.delegateType || d, bt.test(s + d) || (o = o.parentNode);
            o;
            o = o.parentNode
          )
            p.push(o), (a = o)
          a === (n.ownerDocument || E) &&
            p.push(a.defaultView || a.parentWindow || C)
        }
        i = 0
        while ((o = p[i++]) && !e.isPropagationStopped())
          (f = o),
            (e.type = i > 1 ? s : c.bindType || d),
            (l =
              (Y.get(o, 'events') || Object.create(null))[e.type] &&
              Y.get(o, 'handle')) && l.apply(o, t),
            (l = u && o[u]) &&
              l.apply &&
              V(o) &&
              ((e.result = l.apply(o, t)),
              !1 === e.result && e.preventDefault())
        return (
          (e.type = d),
          r ||
            e.isDefaultPrevented() ||
            (c._default && !1 !== c._default.apply(p.pop(), t)) ||
            !V(n) ||
            (u &&
              m(n[d]) &&
              !x(n) &&
              ((a = n[u]) && (n[u] = null),
              (S.event.triggered = d),
              e.isPropagationStopped() && f.addEventListener(d, wt),
              n[d](),
              e.isPropagationStopped() && f.removeEventListener(d, wt),
              (S.event.triggered = void 0),
              a && (n[u] = a))),
          e.result
        )
      }
    },
    simulate(e, t, n) {
      const r = S.extend(new S.Event(), n, { type: e, isSimulated: !0 })
      S.event.trigger(r, null, t)
    },
  }),
    S.fn.extend({
      trigger(e, t) {
        return this.each(function () {
          S.event.trigger(e, t, this)
        })
      },
      triggerHandler(e, t) {
        const n = this[0]
        if (n) return S.event.trigger(e, t, n, !0)
      },
    }),
    y.focusin ||
      S.each({ focus: 'focusin', blur: 'focusout' }, function (n, r) {
        const i = function (e) {
          S.event.simulate(r, e.target, S.event.fix(e))
        }
        S.event.special[r] = {
          setup() {
            const e = this.ownerDocument || this.document || this
            const t = Y.access(e, r)
            t || e.addEventListener(n, i, !0), Y.access(e, r, (t || 0) + 1)
          },
          teardown() {
            const e = this.ownerDocument || this.document || this
            const t = Y.access(e, r) - 1
            t
              ? Y.access(e, r, t)
              : (e.removeEventListener(n, i, !0), Y.remove(e, r))
          },
        }
      })
  const Tt = C.location
  const Ct = { guid: Date.now() }
  const Et = /\?/
  S.parseXML = function (e) {
    let t
    if (!e || typeof e !== 'string') return null
    try {
      t = new C.DOMParser().parseFromString(e, 'text/xml')
    } catch (e) {
      t = void 0
    }
    return (
      (t && !t.getElementsByTagName('parsererror').length) ||
        S.error('Invalid XML: ' + e),
      t
    )
  }
  const St = /\[\]$/
  const kt = /\r?\n/g
  const At = /^(?:submit|button|image|reset|file)$/i
  const Nt = /^(?:input|select|textarea|keygen)/i
  function Dt(n, e, r, i) {
    let t
    if (Array.isArray(e))
      S.each(e, function (e, t) {
        r || St.test(n)
          ? i(n, t)
          : Dt(
              n + '[' + (typeof t === 'object' && t != null ? e : '') + ']',
              t,
              r,
              i
            )
      })
    else if (r || w(e) !== 'object') i(n, e)
    else for (t in e) Dt(n + '[' + t + ']', e[t], r, i)
  }
  ;(S.param = function (e, t) {
    let n
    const r = []
    const i = function (e, t) {
      const n = m(t) ? t() : t
      r[r.length] =
        encodeURIComponent(e) + '=' + encodeURIComponent(n == null ? '' : n)
    }
    if (e == null) return ''
    if (Array.isArray(e) || (e.jquery && !S.isPlainObject(e)))
      S.each(e, function () {
        i(this.name, this.value)
      })
    else for (n in e) Dt(n, e[n], t, i)
    return r.join('&')
  }),
    S.fn.extend({
      serialize() {
        return S.param(this.serializeArray())
      },
      serializeArray() {
        return this.map(function () {
          const e = S.prop(this, 'elements')
          return e ? S.makeArray(e) : this
        })
          .filter(function () {
            const e = this.type
            return (
              this.name &&
              !S(this).is(':disabled') &&
              Nt.test(this.nodeName) &&
              !At.test(e) &&
              (this.checked || !pe.test(e))
            )
          })
          .map(function (e, t) {
            const n = S(this).val()
            return n == null
              ? null
              : Array.isArray(n)
              ? S.map(n, function (e) {
                  return { name: t.name, value: e.replace(kt, '\r\n') }
                })
              : { name: t.name, value: n.replace(kt, '\r\n') }
          })
          .get()
      },
    })
  const jt = /%20/g
  const qt = /#.*$/
  const Lt = /([?&])_=[^&]*/
  const Ht = /^(.*?):[ \t]*([^\r\n]*)$/gm
  const Ot = /^(?:GET|HEAD)$/
  const Pt = /^\/\//
  const Rt = {}
  const Mt = {}
  const It = '*/'.concat('*')
  const Wt = E.createElement('a')
  function Ft(o) {
    return function (e, t) {
      typeof e !== 'string' && ((t = e), (e = '*'))
      let n
      let r = 0
      const i = e.toLowerCase().match(P) || []
      if (m(t))
        while ((n = i[r++]))
          n[0] === '+'
            ? ((n = n.slice(1) || '*'), (o[n] = o[n] || []).unshift(t))
            : (o[n] = o[n] || []).push(t)
    }
  }
  function Bt(t, i, o, a) {
    const s = {}
    const u = t === Mt
    function l(e) {
      let r
      return (
        (s[e] = !0),
        S.each(t[e] || [], function (e, t) {
          const n = t(i, o, a)
          return typeof n !== 'string' || u || s[n]
            ? u
              ? !(r = n)
              : void 0
            : (i.dataTypes.unshift(n), l(n), !1)
        }),
        r
      )
    }
    return l(i.dataTypes[0]) || (!s['*'] && l('*'))
  }
  function $t(e, t) {
    let n
    let r
    const i = S.ajaxSettings.flatOptions || {}
    for (n in t) void 0 !== t[n] && ((i[n] ? e : r || (r = {}))[n] = t[n])
    return r && S.extend(!0, e, r), e
  }
  ;(Wt.href = Tt.href),
    S.extend({
      active: 0,
      lastModified: {},
      etag: {},
      ajaxSettings: {
        url: Tt.href,
        type: 'GET',
        isLocal:
          /^(?:about|app|app-storage|.+-extension|file|res|widget):$/.test(
            Tt.protocol
          ),
        global: !0,
        processData: !0,
        async: !0,
        contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
        accepts: {
          '*': It,
          text: 'text/plain',
          html: 'text/html',
          xml: 'application/xml, text/xml',
          json: 'application/json, text/javascript',
        },
        contents: { xml: /\bxml\b/, html: /\bhtml/, json: /\bjson\b/ },
        responseFields: {
          xml: 'responseXML',
          text: 'responseText',
          json: 'responseJSON',
        },
        converters: {
          '* text': String,
          'text html': !0,
          'text json': JSON.parse,
          'text xml': S.parseXML,
        },
        flatOptions: { url: !0, context: !0 },
      },
      ajaxSetup(e, t) {
        return t ? $t($t(e, S.ajaxSettings), t) : $t(S.ajaxSettings, e)
      },
      ajaxPrefilter: Ft(Rt),
      ajaxTransport: Ft(Mt),
      ajax(e, t) {
        typeof e === 'object' && ((t = e), (e = void 0)), (t = t || {})
        let c
        let f
        let p
        let n
        let d
        let r
        let h
        let g
        let i
        let o
        const v = S.ajaxSetup({}, t)
        const y = v.context || v
        const m = v.context && (y.nodeType || y.jquery) ? S(y) : S.event
        const x = S.Deferred()
        const b = S.Callbacks('once memory')
        let w = v.statusCode || {}
        const a = {}
        const s = {}
        let u = 'canceled'
        var T = {
          readyState: 0,
          getResponseHeader(e) {
            let t
            if (h) {
              if (!n) {
                n = {}
                while ((t = Ht.exec(p)))
                  n[t[1].toLowerCase() + ' '] = (
                    n[t[1].toLowerCase() + ' '] || []
                  ).concat(t[2])
              }
              t = n[e.toLowerCase() + ' ']
            }
            return t == null ? null : t.join(', ')
          },
          getAllResponseHeaders() {
            return h ? p : null
          },
          setRequestHeader(e, t) {
            return (
              h == null &&
                ((e = s[e.toLowerCase()] = s[e.toLowerCase()] || e),
                (a[e] = t)),
              this
            )
          },
          overrideMimeType(e) {
            return h == null && (v.mimeType = e), this
          },
          statusCode(e) {
            let t
            if (e)
              if (h) T.always(e[T.status])
              else for (t in e) w[t] = [w[t], e[t]]
            return this
          },
          abort(e) {
            const t = e || u
            return c && c.abort(t), l(0, t), this
          },
        }
        if (
          (x.promise(T),
          (v.url = ((e || v.url || Tt.href) + '').replace(
            Pt,
            Tt.protocol + '//'
          )),
          (v.type = t.method || t.type || v.method || v.type),
          (v.dataTypes = (v.dataType || '*').toLowerCase().match(P) || ['']),
          v.crossDomain == null)
        ) {
          r = E.createElement('a')
          try {
            ;(r.href = v.url),
              (r.href = r.href),
              (v.crossDomain =
                Wt.protocol + '//' + Wt.host != r.protocol + '//' + r.host)
          } catch (e) {
            v.crossDomain = !0
          }
        }
        if (
          (v.data &&
            v.processData &&
            typeof v.data !== 'string' &&
            (v.data = S.param(v.data, v.traditional)),
          Bt(Rt, v, t, T),
          h)
        )
          return T
        for (i in ((g = S.event && v.global) &&
          S.active++ == 0 &&
          S.event.trigger('ajaxStart'),
        (v.type = v.type.toUpperCase()),
        (v.hasContent = !Ot.test(v.type)),
        (f = v.url.replace(qt, '')),
        v.hasContent
          ? v.data &&
            v.processData &&
            (v.contentType || '').indexOf(
              'application/x-www-form-urlencoded'
            ) === 0 &&
            (v.data = v.data.replace(jt, '+'))
          : ((o = v.url.slice(f.length)),
            v.data &&
              (v.processData || typeof v.data === 'string') &&
              ((f += (Et.test(f) ? '&' : '?') + v.data), delete v.data),
            !1 === v.cache &&
              ((f = f.replace(Lt, '$1')),
              (o = (Et.test(f) ? '&' : '?') + '_=' + Ct.guid++ + o)),
            (v.url = f + o)),
        v.ifModified &&
          (S.lastModified[f] &&
            T.setRequestHeader('If-Modified-Since', S.lastModified[f]),
          S.etag[f] && T.setRequestHeader('If-None-Match', S.etag[f])),
        ((v.data && v.hasContent && !1 !== v.contentType) || t.contentType) &&
          T.setRequestHeader('Content-Type', v.contentType),
        T.setRequestHeader(
          'Accept',
          v.dataTypes[0] && v.accepts[v.dataTypes[0]]
            ? v.accepts[v.dataTypes[0]] +
                (v.dataTypes[0] !== '*' ? ', ' + It + '; q=0.01' : '')
            : v.accepts['*']
        ),
        v.headers))
          T.setRequestHeader(i, v.headers[i])
        if (v.beforeSend && (!1 === v.beforeSend.call(y, T, v) || h))
          return T.abort()
        if (
          ((u = 'abort'),
          b.add(v.complete),
          T.done(v.success),
          T.fail(v.error),
          (c = Bt(Mt, v, t, T)))
        ) {
          if (((T.readyState = 1), g && m.trigger('ajaxSend', [T, v]), h))
            return T
          v.async &&
            v.timeout > 0 &&
            (d = C.setTimeout(function () {
              T.abort('timeout')
            }, v.timeout))
          try {
            ;(h = !1), c.send(a, l)
          } catch (e) {
            if (h) throw e
            l(-1, e)
          }
        } else l(-1, 'No Transport')
        function l(e, t, n, r) {
          let i
          let o
          let a
          let s
          let u
          let l = t
          h ||
            ((h = !0),
            d && C.clearTimeout(d),
            (c = void 0),
            (p = r || ''),
            (T.readyState = e > 0 ? 4 : 0),
            (i = (e >= 200 && e < 300) || e === 304),
            n &&
              (s = (function (e, t, n) {
                let r
                let i
                let o
                let a
                const s = e.contents
                const u = e.dataTypes
                while (u[0] === '*')
                  u.shift(),
                    void 0 === r &&
                      (r = e.mimeType || t.getResponseHeader('Content-Type'))
                if (r)
                  for (i in s)
                    if (s[i] && s[i].test(r)) {
                      u.unshift(i)
                      break
                    }
                if (u[0] in n) o = u[0]
                else {
                  for (i in n) {
                    if (!u[0] || e.converters[i + ' ' + u[0]]) {
                      o = i
                      break
                    }
                    a || (a = i)
                  }
                  o = o || a
                }
                if (o) return o !== u[0] && u.unshift(o), n[o]
              })(v, T, n)),
            !i &&
              S.inArray('script', v.dataTypes) > -1 &&
              (v.converters['text script'] = function () {}),
            (s = (function (e, t, n, r) {
              let i
              let o
              let a
              let s
              let u
              const l = {}
              const c = e.dataTypes.slice()
              if (c[1])
                for (a in e.converters) l[a.toLowerCase()] = e.converters[a]
              o = c.shift()
              while (o)
                if (
                  (e.responseFields[o] && (n[e.responseFields[o]] = t),
                  !u && r && e.dataFilter && (t = e.dataFilter(t, e.dataType)),
                  (u = o),
                  (o = c.shift()))
                )
                  if (o === '*') o = u
                  else if (u !== '*' && u !== o) {
                    if (!(a = l[u + ' ' + o] || l['* ' + o]))
                      for (i in l)
                        if (
                          (s = i.split(' '))[1] === o &&
                          (a = l[u + ' ' + s[0]] || l['* ' + s[0]])
                        ) {
                          !0 === a
                            ? (a = l[i])
                            : !0 !== l[i] && ((o = s[0]), c.unshift(s[1]))
                          break
                        }
                    if (!0 !== a)
                      if (a && e.throws) t = a(t)
                      else
                        try {
                          t = a(t)
                        } catch (e) {
                          return {
                            state: 'parsererror',
                            error: a
                              ? e
                              : 'No conversion from ' + u + ' to ' + o,
                          }
                        }
                  }
              return { state: 'success', data: t }
            })(v, s, T, i)),
            i
              ? (v.ifModified &&
                  ((u = T.getResponseHeader('Last-Modified')) &&
                    (S.lastModified[f] = u),
                  (u = T.getResponseHeader('etag')) && (S.etag[f] = u)),
                e === 204 || v.type === 'HEAD'
                  ? (l = 'nocontent')
                  : e === 304
                  ? (l = 'notmodified')
                  : ((l = s.state), (o = s.data), (i = !(a = s.error))))
              : ((a = l), (!e && l) || ((l = 'error'), e < 0 && (e = 0))),
            (T.status = e),
            (T.statusText = (t || l) + ''),
            i ? x.resolveWith(y, [o, l, T]) : x.rejectWith(y, [T, l, a]),
            T.statusCode(w),
            (w = void 0),
            g && m.trigger(i ? 'ajaxSuccess' : 'ajaxError', [T, v, i ? o : a]),
            b.fireWith(y, [T, l]),
            g &&
              (m.trigger('ajaxComplete', [T, v]),
              --S.active || S.event.trigger('ajaxStop')))
        }
        return T
      },
      getJSON(e, t, n) {
        return S.get(e, t, n, 'json')
      },
      getScript(e, t) {
        return S.get(e, void 0, t, 'script')
      },
    }),
    S.each(['get', 'post'], function (e, i) {
      S[i] = function (e, t, n, r) {
        return (
          m(t) && ((r = r || n), (n = t), (t = void 0)),
          S.ajax(
            S.extend(
              { url: e, type: i, dataType: r, data: t, success: n },
              S.isPlainObject(e) && e
            )
          )
        )
      }
    }),
    S.ajaxPrefilter(function (e) {
      let t
      for (t in e.headers)
        t.toLowerCase() === 'content-type' &&
          (e.contentType = e.headers[t] || '')
    }),
    (S._evalUrl = function (e, t, n) {
      return S.ajax({
        url: e,
        type: 'GET',
        dataType: 'script',
        cache: !0,
        async: !1,
        global: !1,
        converters: { 'text script'() {} },
        dataFilter(e) {
          S.globalEval(e, t, n)
        },
      })
    }),
    S.fn.extend({
      wrapAll(e) {
        let t
        return (
          this[0] &&
            (m(e) && (e = e.call(this[0])),
            (t = S(e, this[0].ownerDocument).eq(0).clone(!0)),
            this[0].parentNode && t.insertBefore(this[0]),
            t
              .map(function () {
                let e = this
                while (e.firstElementChild) e = e.firstElementChild
                return e
              })
              .append(this)),
          this
        )
      },
      wrapInner(n) {
        return m(n)
          ? this.each(function (e) {
              S(this).wrapInner(n.call(this, e))
            })
          : this.each(function () {
              const e = S(this)
              const t = e.contents()
              t.length ? t.wrapAll(n) : e.append(n)
            })
      },
      wrap(t) {
        const n = m(t)
        return this.each(function (e) {
          S(this).wrapAll(n ? t.call(this, e) : t)
        })
      },
      unwrap(e) {
        return (
          this.parent(e)
            .not('body')
            .each(function () {
              S(this).replaceWith(this.childNodes)
            }),
          this
        )
      },
    }),
    (S.expr.pseudos.hidden = function (e) {
      return !S.expr.pseudos.visible(e)
    }),
    (S.expr.pseudos.visible = function (e) {
      return !!(e.offsetWidth || e.offsetHeight || e.getClientRects().length)
    }),
    (S.ajaxSettings.xhr = function () {
      try {
        return new C.XMLHttpRequest()
      } catch (e) {}
    })
  const _t = { 0: 200, 1223: 204 }
  let zt = S.ajaxSettings.xhr()
  ;(y.cors = !!zt && 'withCredentials' in zt),
    (y.ajax = zt = !!zt),
    S.ajaxTransport(function (i) {
      let o, a
      if (y.cors || (zt && !i.crossDomain))
        return {
          send(e, t) {
            let n
            const r = i.xhr()
            if (
              (r.open(i.type, i.url, i.async, i.username, i.password),
              i.xhrFields)
            )
              for (n in i.xhrFields) r[n] = i.xhrFields[n]
            for (n in (i.mimeType &&
              r.overrideMimeType &&
              r.overrideMimeType(i.mimeType),
            i.crossDomain ||
              e['X-Requested-With'] ||
              (e['X-Requested-With'] = 'XMLHttpRequest'),
            e))
              r.setRequestHeader(n, e[n])
            ;(o = function (e) {
              return function () {
                o &&
                  ((o =
                    a =
                    r.onload =
                    r.onerror =
                    r.onabort =
                    r.ontimeout =
                    r.onreadystatechange =
                      null),
                  e === 'abort'
                    ? r.abort()
                    : e === 'error'
                    ? typeof r.status !== 'number'
                      ? t(0, 'error')
                      : t(r.status, r.statusText)
                    : t(
                        _t[r.status] || r.status,
                        r.statusText,
                        (r.responseType || 'text') !== 'text' ||
                          typeof r.responseText !== 'string'
                          ? { binary: r.response }
                          : { text: r.responseText },
                        r.getAllResponseHeaders()
                      ))
              }
            }),
              (r.onload = o()),
              (a = r.onerror = r.ontimeout = o('error')),
              void 0 !== r.onabort
                ? (r.onabort = a)
                : (r.onreadystatechange = function () {
                    r.readyState === 4 &&
                      C.setTimeout(function () {
                        o && a()
                      })
                  }),
              (o = o('abort'))
            try {
              r.send((i.hasContent && i.data) || null)
            } catch (e) {
              if (o) throw e
            }
          },
          abort() {
            o && o()
          },
        }
    }),
    S.ajaxPrefilter(function (e) {
      e.crossDomain && (e.contents.script = !1)
    }),
    S.ajaxSetup({
      accepts: {
        script:
          'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript',
      },
      contents: { script: /\b(?:java|ecma)script\b/ },
      converters: {
        'text script'(e) {
          return S.globalEval(e), e
        },
      },
    }),
    S.ajaxPrefilter('script', function (e) {
      void 0 === e.cache && (e.cache = !1), e.crossDomain && (e.type = 'GET')
    }),
    S.ajaxTransport('script', function (n) {
      let r, i
      if (n.crossDomain || n.scriptAttrs)
        return {
          send(e, t) {
            ;(r = S('<script>')
              .attr(n.scriptAttrs || {})
              .prop({ charset: n.scriptCharset, src: n.url })
              .on(
                'load error',
                (i = function (e) {
                  r.remove(),
                    (i = null),
                    e && t(e.type === 'error' ? 404 : 200, e.type)
                })
              )),
              E.head.appendChild(r[0])
          },
          abort() {
            i && i()
          },
        }
    })
  let Ut
  const Xt = []
  const Vt = /(=)\?(?=&|$)|\?\?/
  S.ajaxSetup({
    jsonp: 'callback',
    jsonpCallback() {
      const e = Xt.pop() || S.expando + '_' + Ct.guid++
      return (this[e] = !0), e
    },
  }),
    S.ajaxPrefilter('json jsonp', function (e, t, n) {
      let r
      let i
      let o
      const a =
        !1 !== e.jsonp &&
        (Vt.test(e.url)
          ? 'url'
          : typeof e.data === 'string' &&
            (e.contentType || '').indexOf(
              'application/x-www-form-urlencoded'
            ) === 0 &&
            Vt.test(e.data) &&
            'data')
      if (a || e.dataTypes[0] === 'jsonp')
        return (
          (r = e.jsonpCallback =
            m(e.jsonpCallback) ? e.jsonpCallback() : e.jsonpCallback),
          a
            ? (e[a] = e[a].replace(Vt, '$1' + r))
            : !1 !== e.jsonp &&
              (e.url += (Et.test(e.url) ? '&' : '?') + e.jsonp + '=' + r),
          (e.converters['script json'] = function () {
            return o || S.error(r + ' was not called'), o[0]
          }),
          (e.dataTypes[0] = 'json'),
          (i = C[r]),
          (C[r] = function () {
            o = arguments
          }),
          n.always(function () {
            void 0 === i ? S(C).removeProp(r) : (C[r] = i),
              e[r] && ((e.jsonpCallback = t.jsonpCallback), Xt.push(r)),
              o && m(i) && i(o[0]),
              (o = i = void 0)
          }),
          'script'
        )
    }),
    (y.createHTMLDocument =
      (((Ut = E.implementation.createHTMLDocument('').body).innerHTML =
        '<form></form><form></form>'),
      Ut.childNodes.length === 2)),
    (S.parseHTML = function (e, t, n) {
      return typeof e !== 'string'
        ? []
        : (typeof t === 'boolean' && ((n = t), (t = !1)),
          t ||
            (y.createHTMLDocument
              ? (((r = (t =
                  E.implementation.createHTMLDocument('')).createElement(
                  'base'
                )).href = E.location.href),
                t.head.appendChild(r))
              : (t = E)),
          (o = !n && []),
          (i = N.exec(e))
            ? [t.createElement(i[1])]
            : ((i = xe([e], t, o)),
              o && o.length && S(o).remove(),
              S.merge([], i.childNodes)))
      let r, i, o
    }),
    (S.fn.load = function (e, t, n) {
      let r
      let i
      let o
      const a = this
      const s = e.indexOf(' ')
      return (
        s > -1 && ((r = vt(e.slice(s))), (e = e.slice(0, s))),
        m(t)
          ? ((n = t), (t = void 0))
          : t && typeof t === 'object' && (i = 'POST'),
        a.length > 0 &&
          S.ajax({ url: e, type: i || 'GET', dataType: 'html', data: t })
            .done(function (e) {
              ;(o = arguments),
                a.html(r ? S('<div>').append(S.parseHTML(e)).find(r) : e)
            })
            .always(
              n &&
                function (e, t) {
                  a.each(function () {
                    n.apply(this, o || [e.responseText, t, e])
                  })
                }
            ),
        this
      )
    }),
    (S.expr.pseudos.animated = function (t) {
      return S.grep(S.timers, function (e) {
        return t === e.elem
      }).length
    }),
    (S.offset = {
      setOffset(e, t, n) {
        let r
        let i
        let o
        let a
        let s
        let u
        const l = S.css(e, 'position')
        const c = S(e)
        const f = {}
        l === 'static' && (e.style.position = 'relative'),
          (s = c.offset()),
          (o = S.css(e, 'top')),
          (u = S.css(e, 'left')),
          (l === 'absolute' || l === 'fixed') && (o + u).includes('auto')
            ? ((a = (r = c.position()).top), (i = r.left))
            : ((a = parseFloat(o) || 0), (i = parseFloat(u) || 0)),
          m(t) && (t = t.call(e, n, S.extend({}, s))),
          t.top != null && (f.top = t.top - s.top + a),
          t.left != null && (f.left = t.left - s.left + i),
          'using' in t
            ? t.using.call(e, f)
            : (typeof f.top === 'number' && (f.top += 'px'),
              typeof f.left === 'number' && (f.left += 'px'),
              c.css(f))
      },
    }),
    S.fn.extend({
      offset(t) {
        if (arguments.length)
          return void 0 === t
            ? this
            : this.each(function (e) {
                S.offset.setOffset(this, t, e)
              })
        let e
        let n
        const r = this[0]
        return r
          ? r.getClientRects().length
            ? ((e = r.getBoundingClientRect()),
              (n = r.ownerDocument.defaultView),
              { top: e.top + n.pageYOffset, left: e.left + n.pageXOffset })
            : { top: 0, left: 0 }
          : void 0
      },
      position() {
        if (this[0]) {
          let e
          let t
          let n
          const r = this[0]
          let i = { top: 0, left: 0 }
          if (S.css(r, 'position') === 'fixed') t = r.getBoundingClientRect()
          else {
            ;(t = this.offset()),
              (n = r.ownerDocument),
              (e = r.offsetParent || n.documentElement)
            while (
              e &&
              (e === n.body || e === n.documentElement) &&
              S.css(e, 'position') === 'static'
            )
              e = e.parentNode
            e &&
              e !== r &&
              e.nodeType === 1 &&
              (((i = S(e).offset()).top += S.css(e, 'borderTopWidth', !0)),
              (i.left += S.css(e, 'borderLeftWidth', !0)))
          }
          return {
            top: t.top - i.top - S.css(r, 'marginTop', !0),
            left: t.left - i.left - S.css(r, 'marginLeft', !0),
          }
        }
      },
      offsetParent() {
        return this.map(function () {
          let e = this.offsetParent
          while (e && S.css(e, 'position') === 'static') e = e.offsetParent
          return e || re
        })
      },
    }),
    S.each(
      { scrollLeft: 'pageXOffset', scrollTop: 'pageYOffset' },
      function (t, i) {
        const o = i === 'pageYOffset'
        S.fn[t] = function (e) {
          return $(
            this,
            function (e, t, n) {
              let r
              if (
                (x(e) ? (r = e) : e.nodeType === 9 && (r = e.defaultView),
                void 0 === n)
              )
                return r ? r[i] : e[t]
              r
                ? r.scrollTo(o ? r.pageXOffset : n, o ? n : r.pageYOffset)
                : (e[t] = n)
            },
            t,
            e,
            arguments.length
          )
        }
      }
    ),
    S.each(['top', 'left'], function (e, n) {
      S.cssHooks[n] = $e(y.pixelPosition, function (e, t) {
        if (t) return (t = Be(e, n)), Me.test(t) ? S(e).position()[n] + 'px' : t
      })
    }),
    S.each({ Height: 'height', Width: 'width' }, function (a, s) {
      S.each(
        { padding: 'inner' + a, content: s, '': 'outer' + a },
        function (r, o) {
          S.fn[o] = function (e, t) {
            const n = arguments.length && (r || typeof e !== 'boolean')
            const i = r || (!0 === e || !0 === t ? 'margin' : 'border')
            return $(
              this,
              function (e, t, n) {
                let r
                return x(e)
                  ? o.indexOf('outer') === 0
                    ? e['inner' + a]
                    : e.document.documentElement['client' + a]
                  : e.nodeType === 9
                  ? ((r = e.documentElement),
                    Math.max(
                      e.body['scroll' + a],
                      r['scroll' + a],
                      e.body['offset' + a],
                      r['offset' + a],
                      r['client' + a]
                    ))
                  : void 0 === n
                  ? S.css(e, t, i)
                  : S.style(e, t, n, i)
              },
              s,
              n ? e : void 0,
              n
            )
          }
        }
      )
    }),
    S.each(
      [
        'ajaxStart',
        'ajaxStop',
        'ajaxComplete',
        'ajaxError',
        'ajaxSuccess',
        'ajaxSend',
      ],
      function (e, t) {
        S.fn[t] = function (e) {
          return this.on(t, e)
        }
      }
    ),
    S.fn.extend({
      bind(e, t, n) {
        return this.on(e, null, t, n)
      },
      unbind(e, t) {
        return this.off(e, null, t)
      },
      delegate(e, t, n, r) {
        return this.on(t, e, n, r)
      },
      undelegate(e, t, n) {
        return arguments.length === 1
          ? this.off(e, '**')
          : this.off(t, e || '**', n)
      },
      hover(e, t) {
        return this.mouseenter(e).mouseleave(t || e)
      },
    }),
    S.each(
      'blur focus focusin focusout resize scroll click dblclick mousedown mouseup mousemove mouseover mouseout mouseenter mouseleave change select submit keydown keypress keyup contextmenu'.split(
        ' '
      ),
      function (e, n) {
        S.fn[n] = function (e, t) {
          return arguments.length > 0 ? this.on(n, null, e, t) : this.trigger(n)
        }
      }
    )
  const Gt = /^[\s\uFEFF\xA0]+|[\s\uFEFF\xA0]+$/g
  ;(S.proxy = function (e, t) {
    let n, r, i
    if ((typeof t === 'string' && ((n = e[t]), (t = e), (e = n)), m(e)))
      return (
        (r = s.call(arguments, 2)),
        ((i = function () {
          return e.apply(t || this, r.concat(s.call(arguments)))
        }).guid = e.guid =
          e.guid || S.guid++),
        i
      )
  }),
    (S.holdReady = function (e) {
      e ? S.readyWait++ : S.ready(!0)
    }),
    (S.isArray = Array.isArray),
    (S.parseJSON = JSON.parse),
    (S.nodeName = A),
    (S.isFunction = m),
    (S.isWindow = x),
    (S.camelCase = X),
    (S.type = w),
    (S.now = Date.now),
    (S.isNumeric = function (e) {
      const t = S.type(e)
      return (t === 'number' || t === 'string') && !isNaN(e - parseFloat(e))
    }),
    (S.trim = function (e) {
      return e == null ? '' : (e + '').replace(Gt, '')
    }),
    typeof define === 'function' &&
      define.amd &&
      define('jquery', [], function () {
        return S
      })
  const Yt = C.jQuery
  const Qt = C.$
  return (
    (S.noConflict = function (e) {
      return C.$ === S && (C.$ = Qt), e && C.jQuery === S && (C.jQuery = Yt), S
    }),
    typeof e === 'undefined' && (C.jQuery = C.$ = S),
    S
  )
})
