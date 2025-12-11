// server/api/send-email.post.ts
import type { H3Event } from 'h3'

/**
 * Proxy that forwards incoming contact form payload to the Vercel email function.
 * No env variables used here — the Vercel function must still have MAIL_USER / MAIL_PASS
 * configured on Vercel itself (those are secret and should not be in this repo).
 */

// Replace this with your actual deployed Vercel function URL (hardcoded by request)
const VERCEL_EMAIL_API = 'https://express-js-on-vercel-six-nu-63.vercel.app/api/send-email'

export default defineEventHandler(async (event: H3Event) => {
  // Only allow POST
  if (event.node.req.method !== 'POST') {
    throw createError({ statusCode: 405, statusMessage: 'Method not allowed' })
  }

  // Read incoming payload
  const body = await readBody(event)

  // Basic validation: ensure there's something to forward
  if (!body || (Object.keys(body).length === 0)) {
    throw createError({ statusCode: 400, statusMessage: 'Empty request body' })
  }

  try {
    // Forward request to Vercel function (no secrets here)
    const resp = await fetch(VERCEL_EMAIL_API, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body),
      // you can add a small timeout here if needed in your hosting environment
    })

    // Read response text (in case it's not JSON)
    const text = await resp.text()
    let json: any = null
    try { json = text ? JSON.parse(text) : null } catch (e) { json = text }

    if (!resp.ok) {
      // Log details server-side for debugging
      console.error('Vercel email API returned error:', resp.status, json)
      throw createError({
        statusCode: resp.status || 502,
        statusMessage: (json && (json.message || json.error)) || 'Remote email service error'
      })
    }

    // Success: return the remote JSON (or a normalized response)
    return json ?? { status: true, message: 'Emails forwarded to Vercel' }
  } catch (err: any) {
    // Log the error for server logs (do not expose internal details to client)
    console.error('send-email proxy failed:', err)
    throw createError({ statusCode: 500, statusMessage: 'Failed to forward email' })
  }
})
