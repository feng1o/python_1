class Solution {
public:
    TreeNode* KthNode(TreeNode* pRoot, unsigned int k)
    {
        if(nullptr == pRoot)
            return nullptr;
        vector<TreeNode*> nvec;
        stack<TreeNode*> stack;
        //stack.push(pRoot);
        TreeNode* node = pRoot;
        while(node != nullptr || !stack.empty()){
            while(node){
                stack.push(node);
                node = node->left;
            }
            node = stack.top();
            stack.pop();
            nvec.push_back(node);
            if(node->right != nullptr){
                //stack.push(node->right);
                node = node->right;
            }
        }
        return (nvec.end() - k);
    }

    
};