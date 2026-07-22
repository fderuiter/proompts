
const disableHiddenPaletteInputs = () => {
  document.querySelectorAll('input.md-option[aria-hidden="true"]').forEach((el) => {
    el.disabled = true;
    el.tabIndex = -1;
  });
};
document.addEventListener("DOMContentLoaded", disableHiddenPaletteInputs);
document.addEventListener("pjax:complete", disableHiddenPaletteInputs);
