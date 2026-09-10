const artifact = document.getElementById('artifact');
const launch = document.getElementById('launch');
const retry = document.getElementById('retry');
const status = document.getElementById('status');
let ready = false;

window.artifactLoadFailed = () => {
  if (ready) return;
  launch.hidden = true;
  retry.hidden = false;
  status.textContent = 'The artifact could not load. Check your connection and try again.';
};
const loadingTimeout = setTimeout(window.artifactLoadFailed, 30000);
retry.addEventListener('click', () => location.reload());
artifact.addEventListener('error', window.artifactLoadFailed);
artifact.addEventListener('load', () => {
  ready = true;
  clearTimeout(loadingTimeout);
  retry.hidden = true;
  launch.hidden = !artifact.canActivateAR;
  launch.disabled = false;
  launch.textContent = 'View in your space';
  status.textContent = artifact.canActivateAR
    ? 'Ready to place. The key is about 18 cm long.'
    : 'Explore the key in 3D here. To try AR, open this page in Safari on iPhone or Chrome on a compatible Android phone.';
});
launch.addEventListener('click', async () => {
  try {
    await artifact.activateAR();
  } catch {
    status.textContent = 'AR could not start. Try Safari on iPhone or Chrome on a compatible Android phone. You can still explore the 3D preview.';
  }
});
artifact.addEventListener('ar-status', (event) => {
  if (event.detail.status === 'failed') {
    status.textContent = 'AR is unavailable on this device right now. You can still rotate and zoom the 3D preview.';
  }
});
