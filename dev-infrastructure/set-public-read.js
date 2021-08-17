// Set public read for both the Firestore + Storage services

const admin = require("firebase-admin");
const fs = require("fs");

const KEY_PATH = "../.keys/cdp-dev.json";

admin.initializeApp({
    credential: admin.credential.cert(KEY_PATH),
});

const keyData = JSON.parse(fs.readFileSync(KEY_PATH));

const PUBLIC_READ_FIRESTORE_RULESET_CONTENT = `
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /{document=**} {
      allow read: if true;
      allow write: if false;
    }
  }
}
`.trim();

const PUBLIC_READ_STORAGE_RULESET_CONTENT = `
rules_version = '2';
service firebase.storage {
  match /b/{bucket}/o {
    match /{allPaths=**} {
      allow read: if true;
      allow write: if false;
    }
  }
}
`.trim();

const securityRules = admin.securityRules();

securityRules.releaseFirestoreRulesetFromSource(
    PUBLIC_READ_FIRESTORE_RULESET_CONTENT
);

securityRules.releaseStorageRulesetFromSource(
    PUBLIC_READ_STORAGE_RULESET_CONTENT,
    `${keyData.project_id}.appspot.com`
);
