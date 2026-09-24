// Client scripts for St. Pete Detective Club: The Sea-Vamp Syndicate
document.addEventListener('DOMContentLoaded', () => {
  const copyTextBtn = document.getElementById('copy-text-btn');
  const toastMsg = document.getElementById('toast-msg');

  const FORM_URL = 'https://docs.google.com/forms/d/e/1FAIpQLSdLydsN0F64kpthBs0-goHsSRrKuIuJPdeTjwRTXw1_v6jwXg/viewform?usp=header';

  function showToast(text) {
    toastMsg.textContent = text;
    toastMsg.classList.add('show');
    setTimeout(() => {
      toastMsg.classList.remove('show');
    }, 2800);
  }

  // Text message template for parents to send
  function getTextInviteMessage() {
    return `Hey! We're organizing a private, adults-only detective adventure in downtown St. Pete with our friends this fall: St. Pete Detective Club — The Sea-Vamp Syndicate!

Think 1920s boomtown mystery meets outdoor city exploration. We'll be in teams of 4 (we'll match everyone up), cracking clues through downtown from ~3:30 to 6:30 PM, ending in time for dinner in Downtown St. Pete (everyone manages their own dinner plans).

It’s $60 a couple for the hosted game and custom case files. We’re polling dates to find the best weekend for everyone (Oct/Nov). 

Take 30 seconds to vote on your available dates on our Google Form:
${FORM_URL}

Hope you guys can make it!`;
  }

  // Copy text template
  if (copyTextBtn) {
    copyTextBtn.addEventListener('click', async () => {
      const msg = getTextInviteMessage();
      try {
        await navigator.clipboard.writeText(msg);
        showToast('📋 Text invite copied with Google Form link!');
      } catch (err) {
        window.prompt('Copy your text invite message below:', msg);
      }
    });
  }
});
