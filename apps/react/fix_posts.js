const fs = require('fs');

let content = fs.readFileSync('src/data/posts.ts', 'utf-8');

// 1. Update the Comment interface
content = content.replace(
`  upvotes: number;
  downvotes: number;`,
`  likes: number;
  isAuthor?: boolean;`
);

// 2. We need to replace upvotes/downvotes ONLY inside comments arrays.
// Because it's hard to do with simple regex, I'll use a trick:
// I'll match objects that have 'replies' or 'isQuestion' or 'parentId', which only comments have.
// Actually, it's easier to just write a script that parses the TS as a string and replaces carefully.
// Let's replace ALL downvotes: X,\n, except the ones inside mockPosts directly.

const mockPostsMatch = content.match(/export const mockPosts: Post\[\] = \[([\s\S]*?)\];\n/);
if (mockPostsMatch) {
  let mockPostsStr = mockPostsMatch[1];
  
  // A naive approach: anything indented with 8+ spaces or 10+ spaces is a comment.
  // In the file, post's upvotes are indented with 4 spaces.
  // Let's check:
  mockPostsStr = mockPostsStr.replace(/^(\s{8,})upvotes: (\d+),/gm, '$1likes: $2,\n$1isAuthor: false,');
  mockPostsStr = mockPostsStr.replace(/^(\s{8,})downvotes: \d+,?\n/gm, '');

  content = content.replace(mockPostsMatch[1], mockPostsStr);
  fs.writeFileSync('src/data/posts.ts', content);
  console.log('Successfully updated posts.ts mock data');
} else {
  console.log('Could not find mockPosts');
}
