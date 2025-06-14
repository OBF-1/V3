export async function generateImage(prompt) {
  const response = await fetch('http://localhost:8000/generate-image', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ prompt })
  });
  return await response.json();
}
