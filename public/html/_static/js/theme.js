!(function (n) {
  const e = {}
  function t(i) {
    if (e[i]) return e[i].exports
    const o = (e[i] = { i, l: !1, exports: {} })
    return n[i].call(o.exports, o, o.exports, t), (o.l = !0), o.exports
  }
  ;(t.m = n),
    (t.c = e),
    (t.d = function (n, e, i) {
      t.o(n, e) || Object.defineProperty(n, e, { enumerable: !0, get: i })
    }),
    (t.r = function (n) {
      typeof Symbol !== 'undefined' &&
        Symbol.toStringTag &&
        Object.defineProperty(n, Symbol.toStringTag, { value: 'Module' }),
        Object.defineProperty(n, '__esModule', { value: !0 })
    }),
    (t.t = function (n, e) {
      if ((1 & e && (n = t(n)), 8 & e)) return n
      if (4 & e && typeof n === 'object' && n && n.__esModule) return n
      const i = Object.create(null)
      if (
        (t.r(i),
        Object.defineProperty(i, 'default', { enumerable: !0, value: n }),
        2 & e && typeof n !== 'string')
      )
        for (const o in n)
          t.d(
            i,
            o,
            function (e) {
              return n[e]
            }.bind(null, o)
          )
      return i
    }),
    (t.n = function (n) {
      const e =
        n && n.__esModule
          ? function () {
              return n.default
            }
          : function () {
              return n
            }
      return t.d(e, 'a', e), e
    }),
    (t.o = function (n, e) {
      return Object.prototype.hasOwnProperty.call(n, e)
    }),
    (t.p = ''),
    t((t.s = 0))
})([
  function (n, e, t) {
    t(1), (n.exports = t(3))
  },
  function (n, e, t) {
    ;(function () {
      const e = typeof window !== 'undefined' ? window.jQuery : t(2)
      ;(n.exports.ThemeNav = {
        navBar: null,
        win: null,
        winScroll: !1,
        winResize: !1,
        linkScroll: !1,
        winPosition: 0,
        winHeight: null,
        docHeight: null,
        isRunning: !1,
        enable(n) {
          const t = this
          void 0 === n && (n = !0),
            t.isRunning ||
              ((t.isRunning = !0),
              e(function (e) {
                t.init(e),
                  t.reset(),
                  t.win.on('hashchange', t.reset),
                  n &&
                    t.win.on('scroll', function () {
                      t.linkScroll ||
                        t.winScroll ||
                        ((t.winScroll = !0),
                        requestAnimationFrame(function () {
                          t.onScroll()
                        }))
                    }),
                  t.win.on('resize', function () {
                    t.winResize ||
                      ((t.winResize = !0),
                      requestAnimationFrame(function () {
                        t.onResize()
                      }))
                  }),
                  t.onResize()
              }))
        },
        enableSticky() {
          this.enable(!0)
        },
        init(n) {
          n(document)
          const e = this
          ;(this.navBar = n('div.wy-side-scroll:first')),
            (this.win = n(window)),
            n(document)
              .on('click', "[data-toggle='wy-nav-top']", function () {
                n("[data-toggle='wy-nav-shift']").toggleClass('shift'),
                  n("[data-toggle='rst-versions']").toggleClass('shift')
              })
              .on('click', '.wy-menu-vertical .current ul li a', function () {
                const t = n(this)
                n("[data-toggle='wy-nav-shift']").removeClass('shift'),
                  n("[data-toggle='rst-versions']").toggleClass('shift'),
                  e.toggleCurrent(t),
                  e.hashChange()
              })
              .on('click', "[data-toggle='rst-current-version']", function () {
                n("[data-toggle='rst-versions']").toggleClass('shift-up')
              }),
            n('table.docutils:not(.field-list,.footnote,.citation)').wrap(
              "<div class='wy-table-responsive'></div>"
            ),
            n('table.docutils.footnote').wrap(
              "<div class='wy-table-responsive footnote'></div>"
            ),
            n('table.docutils.citation').wrap(
              "<div class='wy-table-responsive citation'></div>"
            ),
            n('.wy-menu-vertical ul')
              .not('.simple')
              .siblings('a')
              .each(function () {
                const t = n(this)
                ;(expand = n(
                  '<button class="toctree-expand" title="Open/close menu"></button>'
                )),
                  expand.on('click', function (n) {
                    return e.toggleCurrent(t), n.stopPropagation(), !1
                  }),
                  t.prepend(expand)
              })
        },
        reset() {
          const n = encodeURI(window.location.hash) || '#'
          try {
            const e = $('.wy-menu-vertical')
            let t = e.find('[href="' + n + '"]')
            if (t.length === 0) {
              const i =
                $('.document [id="' + n.substring(1) + '"]').closest(
                  'div.section'
                )((t = e.find('[href="#' + i.attr('id') + '"]'))).length ===
                  0 && (t = e.find('[href="#"]'))
            }
            if (t.length > 0) {
              $('.wy-menu-vertical .current')
                .removeClass('current')
                .attr('aria-expanded', 'false'),
                t.addClass('current').attr('aria-expanded', 'true'),
                t
                  .closest('li.toctree-l1')
                  .parent()
                  .addClass('current')
                  .attr('aria-expanded', 'true')
              for (let n = 1; n <= 10; n++)
                t.closest('li.toctree-l' + n)
                  .addClass('current')
                  .attr('aria-expanded', 'true')
              t[0].scrollIntoView()
            }
          } catch (n) {
            console.log('Error expanding nav for anchor', n)
          }
        },
        onScroll() {
          this.winScroll = !1
          const n = this.win.scrollTop()
          const e = n + this.winHeight
          const t = this.navBar.scrollTop() + (n - this.winPosition)
          n < 0 ||
            e > this.docHeight ||
            (this.navBar.scrollTop(t), (this.winPosition = n))
        },
        onResize() {
          ;(this.winResize = !1),
            (this.winHeight = this.win.height()),
            (this.docHeight = $(document).height())
        },
        hashChange() {
          ;(this.linkScroll = !0),
            this.win.one('hashchange', function () {
              this.linkScroll = !1
            })
        },
        toggleCurrent(n) {
          const e = n.closest('li')
          e
            .siblings('li.current')
            .removeClass('current')
            .attr('aria-expanded', 'false'),
            e
              .siblings()
              .find('li.current')
              .removeClass('current')
              .attr('aria-expanded', 'false')
          const t = e.find('> ul li')
          t.length &&
            (t.removeClass('current').attr('aria-expanded', 'false'),
            e.toggleClass('current').attr('aria-expanded', function (n, e) {
              return e == 'true' ? 'false' : 'true'
            }))
        },
      }),
        typeof window !== 'undefined' &&
          (window.SphinxRtdTheme = {
            Navigation: n.exports.ThemeNav,
            StickyNav: n.exports.ThemeNav,
          }),
        (function () {
          for (
            var n = 0, e = ['ms', 'moz', 'webkit', 'o'], t = 0;
            t < e.length && !window.requestAnimationFrame;
            ++t
          )
            (window.requestAnimationFrame =
              window[e[t] + 'RequestAnimationFrame']),
              (window.cancelAnimationFrame =
                window[e[t] + 'CancelAnimationFrame'] ||
                window[e[t] + 'CancelRequestAnimationFrame'])
          window.requestAnimationFrame ||
            (window.requestAnimationFrame = function (e, t) {
              const i = new Date().getTime()
              const o = Math.max(0, 16 - (i - n))
              const r = window.setTimeout(function () {
                e(i + o)
              }, o)
              return (n = i + o), r
            }),
            window.cancelAnimationFrame ||
              (window.cancelAnimationFrame = function (n) {
                clearTimeout(n)
              })
        })()
    }.call(window))
  },
  function (n, e) {
    n.exports = jQuery
  },
  function (n, e, t) {},
])
