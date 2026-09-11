(() => {
  const box = document.querySelector('.rh-conversation');
  if (!box) return;
  const button = box.querySelector('button');
  const prompt = box.querySelector('textarea');
  const status = box.querySelector('[role="status"]');
  button.hidden = false;
  button.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(prompt.value);
      status.textContent = 'Copied. Paste it into your robot.';
    } catch {
      box.querySelector('details').open = true;
      prompt.focus();
      prompt.select();
      status.textContent = 'Select and copy the prompt below.';
    }
  });
})();
