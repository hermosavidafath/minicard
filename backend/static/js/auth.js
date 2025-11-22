// small helper for show/hide password and basic client validation

// toggle show/hide password
document.addEventListener('click', e => {
  if (e.target.matches('.show-pw')) {
    const wrap = e.target.closest('.pw-wrap')
    const input = wrap && wrap.querySelector('input')
    if (input) {
      input.type = input.type === 'password' ? 'text' : 'password'
      e.target.textContent = input.type === 'password' ? '👁️' : '🙈'
    }
  }
})

// basic required-field check
document.querySelectorAll('.auth-form').forEach(form => {
  form.addEventListener('submit', e => {
    const inputs = Array.from(form.querySelectorAll('input[required], textarea[required]'))
    for (const el of inputs) {
      if (!el.value.trim()) {
        el.focus()
        e.preventDefault()
        return false
      }
    }
  })
})
