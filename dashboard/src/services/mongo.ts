import { MongoClient, ServerApiVersion } from "mongodb";

const uri = String(process.env.MONGODB_URL);
export const client = new MongoClient(uri, {
  serverApi: {
    version: ServerApiVersion.v1,
    strict: true,
    deprecationErrors: true,
  },
});
