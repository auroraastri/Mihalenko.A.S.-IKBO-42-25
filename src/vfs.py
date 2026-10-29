import base64
import os
import xml.etree.ElementTree as ET
from typing import Dict, Optional


class VFSNode:

    def __init__(
        self,
        name: str,
        is_directory: bool = True,
        data: bytes = b"",
    ) -> None:
        self.name = name
        self.is_directory = is_directory
        self.data = data
        self.children: Dict[str, "VFSNode"] = {} if is_directory else {}


class VirtualFileSystem:

    def __init__(self, xml_path: Optional[str] = None) -> None:
        self.xml_path = xml_path
        if xml_path and os.path.exists(xml_path):
            self.root = self._load_from_xml(xml_path)
        else:
            self.root = self._create_default_vfs()

    def _create_default_vfs(self) -> VFSNode:
        root = VFSNode("/", is_directory=True)
        home = VFSNode("home", is_directory=True)
        user = VFSNode("user", is_directory=True)
        sample = VFSNode(
            "sample.txt",
            is_directory=False,
            data=b"Default VFS loaded in memory.",
        )
        user.children["sample.txt"] = sample
        home.children["user"] = user
        root.children["home"] = home
        return root

    def _load_from_xml(self, path: str) -> VFSNode:
        tree = ET.parse(path)
        xml_root = tree.getroot()
        root_node = VFSNode("/", is_directory=True)
        self._populate_node(root_node, xml_root)
        return root_node

    def _populate_node(self, parent_node: VFSNode, xml_elem: ET.Element) -> None:
        for child_elem in xml_elem:
            name = child_elem.attrib.get("name", "unnamed")
            if child_elem.tag == "dir":
                dir_node = VFSNode(name=name, is_directory=True)
                parent_node.children[name] = dir_node
                self._populate_node(dir_node, child_elem)
            elif child_elem.tag == "file":
                raw_text = (child_elem.text or "").strip()
                try:
                    payload = base64.b64decode(raw_text.encode("utf-8"))
                except Exception:
                    payload = raw_text.encode("utf-8")
                file_node = VFSNode(
                    name=name,
                    is_directory=False,
                    data=payload,
                )
                parent_node.children[name] = file_node
