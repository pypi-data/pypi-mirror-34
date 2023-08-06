import ast
import pedal.cait.ast_helpers as ast_str
from types import MethodType


class EasyNode:
	"""
	A wrapper class for AST nodes. Linearizes access to the children of the ast node and saves the field this AST node
	originated from.

	TODO: May want to just add fields and methods to the existing AST nodes and use a production pattern instead.
	"""
	def __init__(self, ast_node, my_field='', tid=0, lin_tree=None, ancestor=None):
		"""
		:param ast_node: The AST node to be wrapped
		:param my_field: the field of the parent node that produced this child.
		"""
		self.children = []
		self.astNode = ast_node
		self.field = my_field
		self.tree_id = tid
		self.parent = ancestor
		if lin_tree is None:
			self.linear_tree = [self]
		else:
			lin_tree.append(self)
			self.linear_tree = lin_tree

		# reference to the easy node wrapping the ast_node
		setattr(ast_node, 'easy_node', self)

		tid_count = tid

		my_field_generator = ast.iter_fields(self.astNode)
		for item in my_field_generator:
			field, value = item
			# if the field doesn't have a value, no child exists
			if value is None:
				continue
			
			# If the children are not in an array, wrap it in an array for consistency in the code the follows
			if type(value) != list:
				value = [value]
			
			# Reference ast_node_visitor.js for the original behavior and keep note of it for the purposes of handling
			# the children noting the special case when the nodes of the array are actually parameters of the node
			# (e.g. a load function) instead of a child node
			for sub_value in value:
				if isinstance(sub_value, ast.AST):
					new_child = EasyNode(sub_value, my_field=field, tid=tid_count + 1, lin_tree=self.linear_tree,
										ancestor=self)
					self.children.append(new_child)
					tid_count = len(self.linear_tree) - 1

	def __str__(self):
		return ''.join([self.field, "\n", ast_str.dump(self.astNode)])

	def numeric_logic_check(self, mag, expr):
		"""
		If this node is a Compare or BoolOp node, sees if the logic in expr (a javascript string being a logical
		statement) matches the logic of self.  This assumes that we are only comparing numerical values to a single
		variable
		TODO: modify this to take multiple variables over multiple BoolOps
		:param mag: the order of magnitude that should be added to numbers to check logic, 1 is usually a good value,
					especially when working with the set of integers.
		:param expr: the "Compare" or "BoolOp" tree to check self against
		:return: True if self (typically student node) and expr are equivalent boolean expressions
		"""
		raise NotImplementedError

	def get_data_type(self):
		# TODO: TIFA
		raise NotImplementedError

	def get_next_tree(self):
		"""Gets the next tree in the AST
		This method gets the next AST node that is of equal or higher level than self. Returns None if the end of the
		tree is reached
		TODO: Create a get sibling method.
		:return: The next tree in the AST
		"""
		# adding function to track tree ids
		def visit_counter(self, node):
			self.counter += 1
			self.generic_visit(node)
		node_counter = ast.NodeVisitor()
		setattr(node_counter, 'counter', self.tree_id)
		node_counter.visit = MethodType(visit_counter, node_counter)

		# getting ids
		node_counter.visit(self.astNode)
		out_of_tree = node_counter.counter >= len(self.linear_tree)  # check if out of bounds
		# len(self.children) > 0 and self.children[-1] == node_counter
		# in_subtree = 0  # check if validly outside of subtree  # TODO: CHECK THIS
		if out_of_tree:
			return None
		return self.linear_tree[node_counter.counter]

	def get_child(self, node):
		"""

		:param node: a non-EasyNode ast node
		:return: the corresponding easy node to the child
		"""
		if isinstance(node, ast.AST):
			for child in self.children:
				if child.astNode == node:
					return child
		elif isinstance(node, int):
			return self.children(node)
		return None

	@staticmethod
	def get_ast_name(node):
		return type(node).__name__

	def __getattr__(self, item):
		if item == 'data_type':
			return self.get_data_type()
		if item == 'next_tree':
			return self.get_next_tree()
		if item == 'ast_name':
			return EasyNode.get_ast_name(self.astNode)
		else:
			if hasattr(self.astNode, item):
				# noinspection PyBroadException
				try:
					field = self.astNode.__getattr__(item)
				except Exception:
					return None
				if EasyNode.get_ast_name(self.astNode) == "Assign" and item == "targets":
					return self.children[0]
				elif isinstance(field, ast.AST):
					return self.get_child(field)
				else:
					return field

	def find_all(self, node_type):
		"""Finds all nodes defined by string node_type

		:param node_type: the string representing the "type" of node to look for
		:return: a list of Ast Nodes (easy_nodes) of self that are of the specified type (including self if self
					meets that criteria)
		"""
		items = []
		visitor = ast.NodeVisitor()
		# setattr(visitor, "current_id", self.tree_id - 1)
		setattr(visitor, "items", items)
		func_name = 'visit_' + node_type

		def main_visit(self, node):
			self.items.append(node.easy_node)
			return self.generic_visit(node)

		func_ref = main_visit
		setattr(visitor, func_name, MethodType(func_ref, visitor))
		visitor.visit(self.astNode)
		return visitor.items


