import Vue from 'vue'

Vue.directive('sidebar-toggle', {
  bind: function (el, binding) {
    function doClose (e) {
      if (!isOpen) return
      if (e === undefined) {
        isOpen = false
        el.classList.remove('show-data')
        document.removeEventListener('click', onClose, false)
      }
    }
    function onClose (e) {
      if (e && el.contains(e.target) && !e.target.classList.contains('close-data') && !e.target.classList.contains('ri-close-fill')) return
      doClose()
    }
    function onOpen () {
      if (isOpen) return
      isOpen = true
      el.classList.add('show-data')
      document.addEventListener('click', onClose, false)
    }
    function onToggle () {
      isOpen ? onClose() : onOpen()
    }
    let isOpen = false
    const toggle = el.querySelector('.iq-user-toggle')
    const dismiss = el.querySelector('#sidebar-dismiss')
    const { value } = binding
    const { click = 'toggle' } = value || {}
    if (click === 'toggle') {
      if (toggle !== null) {
        toggle.addEventListener('click', onToggle, false)
      }
    } else if (click === 'open') {
      if (dismiss !== null) {
        dismiss.addEventListener('click', onOpen, false)
      }
    }
  }
})
